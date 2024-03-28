from django.http import HttpResponseNotFound
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Monitoring, Other, Petition
from login.models import User


class TestsRejectPetition(TestCase):
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

    def testRejectPetitionRedirectReject(self):
        # Hacer una solicitud POST a la vista con el botón "Rechazar"
        response = self.client.post(
            reverse("rejectPetition", kwargs={"petitionId": self.otherWithUser.pk}),
            data={"rechazar": "Rechazar"},
        )

        # Verificar que la solicitud se redirige correctamente
        self.assertRedirects(
            response,
            reverse("showPetition", kwargs={"petitionId": self.otherWithUser.pk}),
        )

    def testRejectPetitionRedirectCancel(self):
        # Hacer una solicitud POST a la vista con el botón "Cancelar"
        response = self.client.post(
            reverse("rejectPetition", kwargs={"petitionId": self.otherWithUser.pk}),
            data={"cancelar": "Cancelar"},
        )

        # Verificar que la solicitud se redirige correctamente
        self.assertRedirects(
            response,
            reverse("showPetition", kwargs={"petitionId": self.otherWithUser.pk}),
        )

    def testRejectPetitionGetMethod(self):
        # Hacer una solicitud GET a la vista
        response = self.client.get(
            reverse("rejectPetition", kwargs={"petitionId": self.otherWithUser.pk})
        )

        # Verificar que la respuesta tiene el código 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar que se está usando la plantilla correcta
        self.assertTemplateUsed(response, "rejectPetition.html")

    def testRejectPetitionInvalidPetitionId(self):
        # Hacer una solicitud POST a la vista con un ID de solicitud inválido
        response = self.client.post(
            reverse("rejectPetition", kwargs={"petitionId": 999}),
            data={"rechazar": "Rechazar"},
        )

        # Verificar que la solicitud devuelve un código de error 404
        self.assertEqual(response.status_code, 404)

    def testRejectPetition(self):
        # Hacer una solicitud POST para rechazar la petición
        response = self.client.post(
            reverse(
                "rejectPetition", kwargs={"petitionId": self.monitoringWithUser.pk}
            ),
            {"rechazar": "Rechazar"},
        )

        # Verificar que la petición ha sido rechazada
        updatedPetition = Monitoring.objects.get(pk=self.monitoringWithUser.pk)
        self.assertEqual(updatedPetition.state, "rechazado")

        # Verificar que la redirección se realiza correctamente
        self.assertRedirects(
            response,
            reverse("showPetition", kwargs={"petitionId": self.monitoringWithUser.pk}),
        )
