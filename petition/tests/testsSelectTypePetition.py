from django.http import HttpResponseNotFound
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Monitoring, Other
from login.models import User


class testsSelectTypePetition(TestCase):
    def setUp(self):
        # Crear un usuario para simular la autenticación
        self.user = User.objects.create(username="testuser", password="testpassword")
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

    def testSelectTypePetitionAuthenticated(self):
        # Hacer una solicitud GET a la vista con un usuario autenticado
        response = self.client.get(reverse("selectTypePetition"))

        # Verificar que la respuesta tenga el código 200 (OK)
        self.assertEqual(response.status_code, 200)

    def testSelectTypePetitionUnauthenticated(self):
        unauthenticatedClient = Client()
        # Hacer una solicitud GET a la vista sin autenticación
        response = unauthenticatedClient.get(reverse("selectTypePetition"))

        # Verificar que la respuesta tenga el código 302 (Redirección a la página de inicio de sesión)
        self.assertEqual(response.status_code, 302)

    def testSelectTypePetitionTemplate(self):
        # Hacer una solicitud GET a la vista con un usuario autenticado
        response = self.client.get(reverse("selectTypePetition"))

        # Verificar que se está utilizando la plantilla correcta
        self.assertTemplateUsed(response, "selectTypePetition.html")

    def testSelectTypePetitionContent(self):
        # Hacer una solicitud GET a la vista con un usuario autenticado
        response = self.client.get(reverse("selectTypePetition"))

        # Verificar que el contenido de la respuesta contiene un texto específico
        self.assertContains(response, "Selecciona el tipo de Solicitud")

    def testSelectTypePetitionContent1(self):
        # Hacer una solicitud GET a la vista con un usuario autenticado
        response = self.client.get(reverse("selectTypePetition"))

        # Verificar que el contenido de la respuesta contiene un texto específico
        self.assertContains(response, "Monitoria")
