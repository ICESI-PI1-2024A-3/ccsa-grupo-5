from django.http import HttpResponseNotFound
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from petition.models import Monitoring, Other
from login.models import User
from django.contrib.auth.models import Group


class TestsSelectTypePetition(TestCase):
    """
    Test suite for selectTypePetition view.
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

        # Create instances of Monitoring and Other for testing
        self.monitoringWithUser = Monitoring.objects.create(
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
        )

        self.otherWithUser = Other.objects.create(
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

        # Petition without user
        self.otherWithoutUser = Other.objects.create(
            petitionDate=timezone.now().date(),
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

    def testSelectTypePetitionAuthenticated(self):
        """
        Test view for selectTypePetition when authenticated.
        """

        # Make a GET request to the view with an authenticated user
        response = self.client.get(reverse("selectTypePetition"))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def testSelectTypePetitionUnauthenticated(self):
        """
        Test view for selectTypePetition when unauthenticated.
        """

        # Create a new client without authentication
        unauthenticatedClient = Client()

        # Make a GET request to the view without authentication
        response = unauthenticatedClient.get(reverse("selectTypePetition"))

        # Check if the response status code is 302 (Redirect to login page)
        self.assertEqual(response.status_code, 302)

    def testSelectTypePetitionTemplate(self):
        """
        Test view for selectTypePetition template.
        """

        # Make a GET request to the view with an authenticated user
        response = self.client.get(reverse("selectTypePetition"))

        # Check if the correct template is being used
        self.assertTemplateUsed(response, "selectTypePetition.html")

    def testSelectTypePetitionContent(self):
        """
        Test view for selectTypePetition content.
        """

        # Make a GET request to the view with an authenticated user
        response = self.client.get(reverse("selectTypePetition"))

        # Check if the response content contains a specific text
        self.assertContains(response, "Seleccione el tipo de solicitud")

    def testSelectTypePetitionContent1(self):
        """
        Test view for selectTypePetition content 1.
        """

        # Make a GET request to the view with an authenticated user
        response = self.client.get(reverse("selectTypePetition"))

        # Check if the response content contains a specific text
        self.assertContains(response, "Monitoria")
