from django.http import HttpResponseNotFound
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Monitoring, Other
from login.models import User
from django.contrib.auth.models import Group


class testsShowPetition(TestCase):
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

    def testShowPetitionOtherExists(self):
        # Hacer una solicitud GET a la vista con una solicitud de Other existente
        response = self.client.get(
            reverse("showPetition", kwargs={"petitionId": self.otherWithUser.pk})
        )

        # Verificar que la respuesta tenga el código 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar que se está usando la plantilla correcta
        self.assertTemplateUsed(response, "viewPetitionO.html")

    def testShowPetitionOtherWithoutUserExists(self):
        # Hacer una solicitud GET a la vista con una solicitud de Other existente
        response = self.client.get(
            reverse("showPetition", kwargs={"petitionId": self.otherWithoutUser.pk})
        )

        # Verificar que la respuesta tenga el código 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar que se está usando la plantilla correcta
        self.assertTemplateUsed(response, "viewPetitionO.html")

    def testShowPetitionMonitoringExists(self):
        # Hacer una solicitud GET a la vista con una solicitud de Monitoring existente
        response = self.client.get(
            reverse("showPetition", kwargs={"petitionId": self.monitoringWithUser.pk})
        )

        # Verificar que la respuesta tenga el código 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar que se está usando la plantilla correcta
        self.assertTemplateUsed(response, "viewPetitionM.html")

    def testShowPetitionNotFound(self):
        # Hacer una solicitud GET a la vista con un ID de solicitud inexistente
        response = self.client.get(reverse("showPetition", kwargs={"petitionId": 999}))

        # Verificar que la respuesta tenga el código 404 (Not Found) en lugar de 200 (OK)
        self.assertEqual(response.status_code, 404)

    def testShowPetitionWithoutLogin(self):
        # Crear un nuevo cliente sin autenticación
        unauthenticatedClient = Client()

        # Hacer una solicitud GET a la vista sin autenticación
        response = unauthenticatedClient.get(
            reverse("showPetition", kwargs={"petitionId": self.otherWithoutUser.pk})
        )

        # Verificar que la respuesta tenga el código 302 (Redirección a la página de inicio de sesión)
        self.assertEqual(response.status_code, 302)
