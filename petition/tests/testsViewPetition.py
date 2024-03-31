from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from ..models import Monitoring, Other
from login.models import User
from django.contrib.auth.models import Group


class testsViewPetition(TestCase):
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

    def testViewAllPetition(self):
        # Hacer una solicitud GET a la vista usando el cliente de prueba
        response = self.client.get(reverse("viewPetition"))

        # Verificar que la respuesta tenga el código 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar que el contexto de la respuesta contenga las peticiones
        self.assertIn("petitions", response.context)

        # Verificar que las peticiones en el contexto son las esperadas
        expected_petitions = [
            self.monitoringWithUser,
            self.otherWithUser,
            self.otherWithoutUser,
        ]
        actual_petitions = list(response.context["petitions"])
        self.assertEqual(len(expected_petitions), len(actual_petitions))
        self.assertListEqual(expected_petitions, actual_petitions)

    def testViewPetitionWithoutUserAuthenticated(self):
        # Hacer una solicitud GET a la vista con un usuario autenticado
        response = self.client.get(reverse("viewPetition"))

        # Verificar que la respuesta tenga el código 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar que el usuario autenticado está presente en la vista
        self.assertIn("user", response.context)
        self.assertEqual(response.context["user"], self.user)

    def testViewPetitionWithoutUserUnauthenticated(self):
        # Crear un nuevo cliente sin autenticación
        unauthenticatedClient = Client()

        # Hacer una solicitud GET a la vista sin autenticación
        response = unauthenticatedClient.get(reverse("viewPetition"))

        # Verificar que la respuesta tenga el código 302 (Redirección a la página de inicio de sesión)
        self.assertEqual(response.status_code, 302)

    def testViewPetitionWithoutUserEmptyQueryset(self):
        # Eliminar todas las instancias de Monitoring y Other para simular un queryset vacío
        Monitoring.objects.all().delete()
        Other.objects.all().delete()

        # Hacer una solicitud GET a la vista con un usuario autenticado
        response = self.client.get(reverse("viewPetition"))

        # Verificar que la respuesta tenga el código 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar que el contexto de la respuesta contenga las peticiones vacías
        self.assertIn("petitions", response.context)

    def testViewPetitionInvalidUser(self):
        # Crear un nuevo usuario no existente en la base de datos
        invalidUser = User(id="1", username="invaliduser", password="invalidpassword")

        # Hacer una solicitud GET a la vista con el usuario no existente
        self.client.force_login(invalidUser)
        response = self.client.get(reverse("viewPetition"))

        # Verificar que la respuesta tenga el código 302 (Redirección a la página de inicio de sesión)
        self.assertEqual(response.status_code, 302)
