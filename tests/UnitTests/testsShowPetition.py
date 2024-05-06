from django.http import HttpResponseNotFound
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from petition.models import Monitoring, Other
from login.models import User
from django.contrib.auth.models import Group

class TestsShowPetition(TestCase):
    """
    Test suite for showPetition views.
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

    def testShowPetitionOtherExists(self):
        """
        Test view for showing Other petition when it exists.
        """

        # Make a GET request to the view with an existing Other petition
        response = self.client.get(
            reverse("showPetition", kwargs={"petitionId": self.otherWithUser.pk})
        )

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is being used
        self.assertTemplateUsed(response, "viewPetitionO.html")

    def testShowPetitionOtherWithoutUserExists(self):
        """
        Test view for showing Other petition without user when it exists.
        """

        # Make a GET request to the view with an existing Other petition
        response = self.client.get(
            reverse("showPetition", kwargs={"petitionId": self.otherWithoutUser.pk})
        )

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is being used
        self.assertTemplateUsed(response, "viewPetitionO.html")

    def testShowPetitionMonitoringExists(self):
        """
        Test view for showing Monitoring petition when it exists.
        """

        # Make a GET request to the view with an existing Monitoring petition
        response = self.client.get(
            reverse("showPetition", kwargs={"petitionId": self.monitoringWithUser.pk})
        )

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is being used
        self.assertTemplateUsed(response, "viewPetitionM.html")

    def testShowPetitionNotFound(self):
        """
        Test view for showing petition when it does not exist.
        """

        # Make a GET request to the view with a non-existing petition ID
        response = self.client.get(reverse("showPetition", kwargs={"petitionId": 999}))

        # Check if the response status code is 404 (Not Found) instead of 200 (OK)
        self.assertEqual(response.status_code, 404)

    def testShowPetitionWithoutLogin(self):
        """
        Test view for showing petition without login.
        """

        # Create a new client without authentication
        unauthenticatedClient = Client()

        # Make a GET request to the view without authentication
        response = unauthenticatedClient.get(
            reverse("showPetition", kwargs={"petitionId": self.otherWithoutUser.pk})
        )

        # Check if the response status code is 302 (Redirect to login page)
        self.assertEqual(response.status_code, 302)
