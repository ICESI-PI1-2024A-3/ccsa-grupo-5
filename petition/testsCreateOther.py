from django.test import TestCase, Client
from django.urls import reverse
from petition.forms.createNewOtherPetition import CreateNewOtherPetition
from .models import Other
from login.models import User
from django.utils import timezone
from django.contrib.auth.models import Group


class TestCreateOther(TestCase):
    """
    Test suite for create other petition view.
    """

    def setUp(self):
        """
        Set up data for each test.
        """
        
        # Create groups for permissions
        gestorGroup, _ = Group.objects.get_or_create(name="Gestor de Contratacion")
        liderGroup, _ = Group.objects.get_or_create(name="Lider de Proceso")
        admin, _ = Group.objects.get_or_create(name="Admin")

        # Create a user to simulate authentication
        Group.objects.get_or_create(name="Admin")
        self.user = User.objects.create(username="testuser", password="testpassword")
        group = Group.objects.get(name="Admin")
        self.user.groups.add(group)
        self.client = Client()
        self.client.force_login(self.user)

    def testCreateOtherGet(self):
        """
        Test GET request to create other petition view.
        """

        response = self.client.get(reverse("createOther"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "createOther.html")
        self.assertIsInstance(response.context["form"], CreateNewOtherPetition)

    def testCreateOtherPostWithPermissions(self):
        """
        Test POST request to create other petition view with proper permissions.
        """

        response = self.client.post(
            reverse("createOther"),
            {
                "startDate": timezone.now().date(),
                "endDate": timezone.now().date() + timezone.timedelta(days=30),
                "state": "pendiente",
                "cenco": "Cenco de ejemplo",
                "fullName": "Nombre de ejemplo",
                "identityDocument": "1234567890",
                "email": "ejemplo@correo.com",
                "phoneNumber": "123456789",
                "personType": "serviceProvision",
                "requesterName": "Nombre del solicitante",
                "requesterFaculty": "Facultad del solicitante",
                "motive": "Motivo de la petición",
                "bankEntity": "Entidad bancaria",
                "bankAccountType": "Ahorro",
                "bankAccountNumber": "1234567890",
                "eps": "EPS del solicitante",
                "pensionFund": "Fondo de pensiones del solicitante",
                "arl": "ARL del solicitante",
                "contractValue": 1000.00,
                "paymentInfo": "Información de pago",
                "rutAttachment": "ruta/del/archivo/rut.pdf",
            },
        )
        self.assertEqual(response.status_code, 200)

        Other.objects.filter(
                startDate=timezone.now().date(),
                endDate=timezone.now().date() + timezone.timedelta(days=30),
                state="pendiente",
                cenco="Cenco de ejemplo",
                fullName="Nombre de ejemplo",
                identityDocument="1234567890",
                email="ejemplo@correo.com",
                phoneNumber="123456789",
                personType="serviceProvision",
                requesterName="Nombre del solicitante",
                requesterFaculty="Facultad del solicitante",
                motive="Motivo de la petición",
                bankEntity="Entidad bancaria",
                bankAccountType="Ahorro",
                bankAccountNumber="1234567890",
                eps="EPS del solicitante",
                pensionFund="Fondo de pensiones del solicitante",
                arl="ARL del solicitante",
                contractValue=1000.00,
                paymentInfo="Información de pago",
                rutAttachment="ruta/del/archivo/rut.pdf",
            ).exists()
        

    def testCreateOtherPostWithoutUser(self):
        """
        Test POST request to create other petition view without proper permissions.
        """

        self.user.groups.clear()  # Remove all groups from user
        response = self.client.post(
            reverse("createOther"),
            {
                "startDate": timezone.now().date(),
                "endDate": timezone.now().date() + timezone.timedelta(days=30),
                "state": "pendiente",
                "cenco": "Cenco de ejemplo",
                "fullName": "Nombre de ejemplo",
                "identityDocument": "1234567890",
                "email": "ejemplo@correo.com",
                "phoneNumber": "123456789",
                "personType": "serviceProvision",
                "requesterName": "Nombre del solicitante",
                "requesterFaculty": "Facultad del solicitante",
                "motive": "Motivo de la petición",
                "bankEntity": "Entidad bancaria",
                "bankAccountType": "Ahorro",
                "bankAccountNumber": "1234567890",
                "eps": "EPS del solicitante",
                "pensionFund": "Fondo de pensiones del solicitante",
                "arl": "ARL del solicitante",
                "contractValue": 1000.00,
                "paymentInfo": "Información de pago",
                "rutAttachment": "ruta/del/archivo/rut.pdf",
            },
        )
        self.assertEqual(response.status_code, 302)  # Forbidden

    def testCreateOtherPostInvalidForm(self):
        """
        Test POST request to create other petition view with invalid form data.
        """
        response = self.client.post(reverse("createOther"), {})
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertTrue('startDate' in form.errors)
        self.assertEqual(form.errors['startDate'], ["Este campo es obligatorio."])


    def testCreateOtherPostRedirect(self):
        """
        Test redirection for POST request to create other petition view when not logged in.
        """

        # Ensure redirection if not logged in
        self.client.logout()
        response = self.client.post(reverse("createOther"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)
