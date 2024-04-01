from django.test import TestCase, Client
from django.urls import reverse
from ..models import Monitoring, Other, Observation, Petition
from login.models import User
from django.utils import timezone
from django.contrib.auth.models import Group


class TestDeletePetition(TestCase):
    """
    Test suite for delete petition view.
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

        self.observation = Observation.objects.create(
            description="Observación de ejemplo",
            date="2024-04-01",
            time="12:00:00",
            author="",
            petition=self.monitoringWithUser,
        )

    def testDeletePetitionPostMWithUser(self):
        """
        Test for deleting a Monitoring petition with a user associated.
        """

        response = self.client.post(
            reverse("deletePetition", args=[self.monitoringWithUser.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("viewPetition"))
        with self.assertRaises(Petition.DoesNotExist):
            Petition.objects.get(pk=self.monitoringWithUser.pk)

    def testDeletePetitionPostOWithoutUser(self):
        """
        Test for deleting an Other petition without a user associated.
        """

        response = self.client.post(
            reverse("deletePetition", args=[self.otherWithoutUser.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("viewPetition"))
        with self.assertRaises(Petition.DoesNotExist):
            Petition.objects.get(pk=self.otherWithoutUser.pk)

    def testDeletePetitionPostOWithUser(self):
        """
        Test for deleting an Other petition with a user associated.
        """

        response = self.client.post(
            reverse("deletePetition", args=[self.otherWithUser.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("viewPetition"))
        with self.assertRaises(Petition.DoesNotExist):
            Petition.objects.get(pk=self.otherWithUser.pk)

    def testDeletePetitionPostRedirect(self):
        """
        Test redirection if not logged in.
        """

        # Ensure redirection if not logged in
        self.client.logout()
        response = self.client.post(
            reverse("deletePetition", args=[self.monitoringWithUser.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)

    def testDeletePetitionPostNotFound(self):
        """
        Test for deletion of a non-existent petition.
        """

        response = self.client.post(reverse("deletePetition", args=[999]))
        self.assertEqual(response.status_code, 404)
