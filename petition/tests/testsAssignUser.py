from django.http import HttpResponseNotFound
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Monitoring, Other, Observation, Petition
from login.models import User
from django.contrib.auth.models import Group


class testAssignUser(TestCase):
    def setUp(self):
        # Crear un usuario para simular la autenticación
        Group.objects.get_or_create(name="Admin")
        self.user = User.objects.create(username="testuser", password="testpassword")
        group = Group.objects.get(name="Admin")
        self.user.groups.add(group)
        self.client = Client()
        self.client.force_login(self.user)

        # Crear instancias de Monitoring y Other para usar en las pruebas
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

        self.observationMonitoring = Observation.objects.create(
            description="Observación de ejemplo",
            date="2024-04-01",
            time="12:00:00",
            author="",
            petition=self.monitoringWithUser,
        )

        self.observationOtherWithoutUser = Observation.objects.create(
            description="Observación de ejemplo",
            date="2024-04-01",
            time="12:00:00",
            author="",
            petition=self.otherWithoutUser,
        )

        self.observationOtherWithUser = Observation.objects.create(
            description="Observación de ejemplo",
            date="2024-04-01",
            time="12:00:00",
            author="",
            petition=self.otherWithUser,
        )

    def testAssignUserToPetitionPostAssign(self):
        response = self.client.post(
            reverse("assignPetition", args=[self.otherWithUser.pk]),
            {"assign": "Assign", "user": self.user.pk},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.otherWithUser.user, self.user)

    def testAssignUserToPetitionPostCancel(self):
        response = self.client.post(
            reverse("assignPetition", args=[self.otherWithoutUser.pk]),
            {"cancel": "Cancel"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(self.otherWithoutUser.user, self.user)

    def testAssignUserToPetitionGet(self):
        response = self.client.get(
            reverse("assignPetition", args=[self.otherWithUser.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "assignUserToPetition.html")
        self.assertIn("petition", response.context)
        self.assertIn("users", response.context)

    def testAssignUserToPetitionPostInvalidUser(self):
        with self.assertRaises(User.DoesNotExist):
            self.client.post(
                reverse("assignPetition", args=[self.otherWithUser.pk]),
                {"assign": "Assign", "user": "544545"},
            )

    def testAssignUserToPetitionPostInvalidPetition(self):
        with self.assertRaises(Petition.DoesNotExist):
            self.client.post(
                reverse("assignPetition", args=[999]),
                {"assign": "Assign", "user": self.user.pk},
            )
