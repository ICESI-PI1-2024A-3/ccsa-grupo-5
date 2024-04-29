from django.http import HttpResponseNotFound
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from .models import Monitoring, Other, Petition
from login.models import User
from django.contrib.auth.models import Group


class TestsRejectPetition(TestCase):
    """
    Test suite for rejectPetition view.
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

    def testRejectPetitionRedirectReject(self):
        """
        Test view for rejecting a petition and redirecting to showPetition.
        """

        # Make a POST request to the view with the "Reject" button
        response = self.client.post(
            reverse("rejectPetition", kwargs={"petitionId": self.otherWithUser.pk}),
            data={"rechazar": "Rechazar"},
        )

        # Check if the request redirects correctly
        self.assertRedirects(
            response,
            reverse("showPetition", kwargs={"petitionId": self.otherWithUser.pk}),
        )

    def testRejectPetitionRedirectCancel(self):
        """
        Test view for cancelling a petition rejection and redirecting to showPetition.
        """

        # Make a POST request to the view with the "Cancel" button
        response = self.client.post(
            reverse("rejectPetition", kwargs={"petitionId": self.otherWithUser.pk}),
            data={"cancelar": "Cancelar"},
        )

        # Check if the request redirects correctly
        self.assertRedirects(
            response,
            reverse("showPetition", kwargs={"petitionId": self.otherWithUser.pk}),
        )

    def testRejectPetitionGetMethod(self):
        """
        Test view for accessing the rejectPetition page with GET method.
        """

        # Make a GET request to the view
        response = self.client.get(
            reverse("rejectPetition", kwargs={"petitionId": self.otherWithUser.pk})
        )

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is being used
        self.assertTemplateUsed(response, "rejectPetition.html")

    def testRejectPetitionInvalidPetitionId(self):
        """
        Test view for rejecting a petition with an invalid petition ID.
        """

        # Make a POST request to the view with an invalid petition ID
        response = self.client.post(
            reverse("rejectPetition", kwargs={"petitionId": 999}),
            data={"rechazar": "Rechazar"},
        )

        # Check if the request returns a 404 error code
        self.assertEqual(response.status_code, 404)

    def testRejectPetition(self):
        """
        Test view for rejecting a petition.
        """

        # Make a POST request to reject the petition
        response = self.client.post(
            reverse(
                "rejectPetition", kwargs={"petitionId": self.monitoringWithUser.pk}
            ),
            {"rechazar": "Rechazar"},
        )

        # Check if the petition has been rejected
        updatedPetition = Monitoring.objects.get(pk=self.monitoringWithUser.pk)
        self.assertEqual(updatedPetition.state, "rechazado")

        # Check if the redirection is performed correctly
        self.assertRedirects(
            response,
            reverse("showPetition", kwargs={"petitionId": self.monitoringWithUser.pk}),
        )
