from django.test import TestCase, Client
from django.urls import reverse
from petition.forms.createNewObservation import CreateNewObservation
from petition.models import Observation, Other ,Monitoring
from login.models import User
from django.utils import timezone
from django.contrib.auth.models import Group


class TestCreateObservation(TestCase):
    """
    Test suite for create observation view.
    """

    def setUp(self):
        """
        Set up data for each test.
        """

        # Create a user to simulate authentication
        Group.objects.get_or_create(name="Admin")
        self.user = User.objects.create(username="testuser", password="testpassword")
        group = Group.objects.get(name="Admin")
        self.user.groups.add(group)
        self.client = Client()
        self.client.force_login(self.user)

        # Create instances of Monitoring and Other for use in tests
        self.monitoringWithUser = Monitoring.objects.create(
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
        )

        self.otherWithUser = Other.objects.create(
            startDate=timezone.now().date(),
            endDate=timezone.now().date() + timezone.timedelta(days=30),
            state="pendiente",
            cenco="Cenco de ejemplo",
            fullName="Nombre de ejemplo",
            identityDocument="1234567890",
            email="ejemplo@correo.com",
            phoneNumber="123456789",
            user=self.user,
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
        )

        # Solicitud sin usuario
        self.otherWithoutUser = Other.objects.create(
            startDate=timezone.now().date(),
            endDate=timezone.now().date() + timezone.timedelta(days=40),
            state="pendiente",
            cenco="Cenco de ejemplo",
            fullName="Nombre de ejemplo",
            identityDocument="1234567890",
            email="ejemplo@correo.com",
            phoneNumber="123456789",
            user=None,
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
        )

        self.observation = Observation.objects.create(
            description="Observación de ejemplo",
            date="2024-04-01",
            time="12:00:00",
            author=self.user,
            petition=self.monitoringWithUser,
        )

    def testCreateObservationAuthenticated(self):
        """
        Test GET request to create observation view when authenticated.
        """

        response = self.client.get(
            reverse("createObservation", kwargs={"petitionId": self.monitoringWithUser.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "createObservation.html")
        self.assertIsInstance(response.context["form"], CreateNewObservation)
        self.assertEqual(response.context["petitionId"], self.monitoringWithUser.id)

    def testCreateObservationUnauthenticated(self):
        """
        Test GET request to create observation view when unauthenticated.
        """

        self.client.logout()
        response = self.client.get(
            reverse("createObservation", kwargs={"petitionId": self.monitoringWithUser.id})
        )
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def testCreateObservationPostValid(self):
        """
        Test POST request to create observation view with valid data.
        """

        response = self.client.post(
            reverse("createObservation", kwargs={"petitionId": self.monitoringWithUser.id}),
            data={
                "description": "Nueva observación",
                "date": "2024-04-01",
                "time": "12:00:00",
            },
        )
        self.assertEqual(response.status_code, 302)  # Redirect after successful POST
        self.assertEqual(Observation.objects.count(), 2)  # Check if observation was created

    def testCreateObservationPostInvalid(self):
        """
        Test POST request to create observation view with invalid data.
        """

        response = self.client.post(
            reverse("createObservation", kwargs={"petitionId": self.monitoringWithUser.id}),
            data={},
        )
        self.assertEqual(
            response.status_code, 200
        )  # Stay on the same page after invalid POST
        form = response.context['form']  
        self.assertFalse(form.is_valid()) 
        self.assertTrue('description' in form.errors)  

    def testCreateObservationPermission(self):
        """
        Test permissions for create observation view.
        """

        self.user.groups.add(Group.objects.create(name="Lider de Proceso"))
        response = self.client.get(
            reverse("createObservation", kwargs={"petitionId": self.monitoringWithUser.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "createObservation.html")
