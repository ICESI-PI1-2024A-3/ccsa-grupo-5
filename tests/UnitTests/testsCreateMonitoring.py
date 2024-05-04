from django.http import HttpResponseNotFound
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse

from petition.forms.createNewMonitoringPetition import CreateNewMonitoringPetition
from petition.forms.createNewOtherPetition import CreateNewOtherPetition
from petition.models import Monitoring, Other, Observation, Petition
from login.models import User
from django.contrib.auth.models import Group


class testsCreateMonitoring(TestCase):
    """
    Test suite for the create monitoring view.
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

    def testCreateMonitoringGet(self):
        """
        Test GET request to create monitoring view.
        """
        response = self.client.get(reverse("createMonitoring"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "createMonitoring.html")
        self.assertIsInstance(response.context["form"], CreateNewMonitoringPetition)

    def testCreateMonitoringPostWithPermissions(self):
        """
        Test POST request to create monitoring view with permissions.
        """
        response = self.client.post(
            reverse("createMonitoring"),
            {
                "petitionDate": timezone.now().date(),
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

        Monitoring.objects.filter(
            petitionDate=timezone.now().date(),
            startDate=timezone.now().date(),
            endDate=timezone.now().date() + timezone.timedelta(days=30),
            state="pendiente",
            cenco="Cenco de ejemplo",
            fullName="Nombre de ejemplo",
            identityDocument="1234567890",
            email="ejemplo@correo.com",
            phoneNumber="123456789",
            user=self.user,
            monitoringType="academica",
            hasMoneyInCenco=True,
            cencoResponsible="Responsable de Cenco",
            studentCode="ABC123",
            daviPlata="DAVI123",
            projectOrCourse="Proyecto o Curso de ejemplo",
            monitoringDescription="Descripción de la monitoria",
            hoursPerWeek=10,
            totalPaymentAmount=500.00,
            isOneTimePayment=False,
        ).exists()

    def testCreateMonitoringPostWithoutUser(self):
        """
        Test POST request to create monitoring view without user.
        """
        self.user.groups.clear()  # Remove all groups from user
        response = self.client.post(
            reverse("createMonitoring"),
            {
                "petitionDate": timezone.now().date(),
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

    def testCreateMonitoringPostInvalidForm(self):
        """
        Test POST request to create monitoring view with invalid form data.
        """
        response = self.client.post(reverse("createMonitoring"), {})
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertTrue('startDate' in form.errors)
        self.assertEqual(form.errors['startDate'], ["Este campo es obligatorio."])

    def testCreateMonitoringPostRedirect(self):
        """
        Test redirection for POST request to create monitoring view when not logged in.
        """
        self.client.logout()
        response = self.client.post(reverse("createMonitoring"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)
