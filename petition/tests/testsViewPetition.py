from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from ..models import Monitoring, Other
from login.models import User
from django.contrib.auth.models import Group

class TestsViewPetition(TestCase):
    """
    Test suite for viewPetition views.
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

        # Petition without user
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

    def testViewAllPetition(self):
        """
        Test view for all petitions.
        """

        # Make a GET request to the view using the test client
        response = self.client.get(reverse("viewPetition"))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response context contains the petitions
        self.assertIn("petitions", response.context)

        # Check if the petitions in the context are as expected
        expected_petitions = [
            self.monitoringWithUser,
            self.otherWithUser,
            self.otherWithoutUser,
        ]
        actual_petitions = list(response.context["petitions"])
        self.assertEqual(len(expected_petitions), len(actual_petitions))
        self.assertListEqual(expected_petitions, actual_petitions)

    def testViewPetitionWithoutUserAuthenticated(self):
        """
        Test view for petition without user with authenticated user.
        """

        # Make a GET request to the view with an authenticated user
        response = self.client.get(reverse("viewPetition"))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the authenticated user is present in the view
        self.assertIn("user", response.context)
        self.assertEqual(response.context["user"], self.user)

    def testViewPetitionWithoutUserUnauthenticated(self):
        """
        Test view for petition without user with unauthenticated user.
        """

        # Create a new client without authentication
        unauthenticatedClient = Client()

        # Make a GET request to the view without authentication
        response = unauthenticatedClient.get(reverse("viewPetition"))

        # Check if the response status code is 302 (Redirect to login page)
        self.assertEqual(response.status_code, 302)

    def testViewPetitionWithoutUserEmptyQueryset(self):
        """
        Test view for petition without user with empty queryset.
        """

        # Delete all instances of Monitoring and Other to simulate an empty queryset
        Monitoring.objects.all().delete()
        Other.objects.all().delete()

        # Make a GET request to the view with an authenticated user
        response = self.client.get(reverse("viewPetition"))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response context contains the empty petitions
        self.assertIn("petitions", response.context)
        self.assertListEqual(list(response.context["petitions"]), [])

    def testViewPetitionInvalidUser(self):
        """
        Test view for petition with invalid user.
        """

        # Create a new user not existing in the database
        invalidUser = User(id="1", username="invaliduser", password="invalidpassword")

        # Make a GET request to the view with the non-existing user
        self.client.force_login(invalidUser)
        response = self.client.get(reverse("viewPetition"))

        # Check if the response status code is 302 (Redirect to login page)
        self.assertEqual(response.status_code, 302)