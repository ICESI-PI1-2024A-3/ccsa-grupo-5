from django.http import HttpResponseNotFound
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from petition.models import Monitoring, Other, Observation, Petition
from login.models import User
from django.contrib.auth.models import Group


class testAssignUser(TestCase):
    """
    Test suite for the assign user view.
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

        # Create instances of Monitoring, Other, and Observation for use in tests
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

        # Create observations for monitoring and other petitions
        self.observationMonitoring = Observation.objects.create(
            description="Observación de ejemplo",
            date="2024-04-01",
            time="12:00:00",
            author=self.user,
            petition=self.monitoringWithUser,
        )

        self.observationOtherWithoutUser = Observation.objects.create(
            description="Observación de ejemplo",
            date="2024-04-01",
            time="12:00:00",
            author=self.user,
            petition=self.otherWithoutUser,
        )

        self.observationOtherWithUser = Observation.objects.create(
            description="Observación de ejemplo",
            date="2024-04-01",
            time="12:00:00",
            author=self.user,
            petition=self.otherWithUser,
        )

    def testAssignUserToPetitionPostAssign(self):
        """
        Test POST request to assign user to petition.
        """
        response = self.client.post(
            reverse("assignPetition", args=[self.otherWithUser.pk]),
            {"assign": "Assign", "user": self.user.pk},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.otherWithUser.user, self.user)

    def testAssignUserToPetitionPostCancel(self):
        """
        Test POST request to cancel assignment of user to petition.
        """
        response = self.client.post(
            reverse("assignPetition", args=[self.otherWithoutUser.pk]),
            {"cancel": "Cancel"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(self.otherWithoutUser.user, self.user)

    def testAssignUserToPetitionGet(self):
        """
        Test GET request to assign user to petition.
        """
        response = self.client.get(
            reverse("assignPetition", args=[self.otherWithUser.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "assignUserToPetition.html")
        self.assertIn("petition", response.context)
        self.assertIn("users", response.context)

    def testAssignUserToPetitionPostInvalidUser(self):
        """
        Test POST request to assign invalid user to petition.
        """
        with self.assertRaises(User.DoesNotExist):
            self.client.post(
                reverse("assignPetition", args=[self.otherWithUser.pk]),
                {"assign": "Assign", "user": "544545"},
            )

    def testAssignUserToPetitionPostInvalidPetition(self):
        """
        Test POST request to assign user to invalid petition.
        """
        with self.assertRaises(Petition.DoesNotExist):
            self.client.post(
                reverse("assignPetition", args=[999]),
                {"assign": "Assign", "user": self.user.pk},
            )
