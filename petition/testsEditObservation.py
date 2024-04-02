from django.test import TestCase, Client
from django.urls import reverse
from .models import Monitoring, Other, Observation
from login.models import User
from django.utils import timezone
from django.contrib.auth.models import Group


class TestEditObservationView(TestCase):
    """
    Test suite for edit observation view.
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
        self.monitoring_with_user = Monitoring.objects.create(
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

        self.observation = Observation.objects.create(
            description="Observación de ejemplo",
            date="2024-04-01",
            time="12:00:00",
            author="",
            petition=self.monitoring_with_user,
        )

    def testEditObservationAuthenticatedGet(self):
        """
        Test for authenticated user accessing edit observation view using GET method.
        """

        response = self.client.get(
            reverse(
                "editObservation",
                kwargs={
                    "petitionId": self.monitoring_with_user.id,
                    "observationId": self.observation.id,
                },
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "editObservation.html")

    def testEditObservationAuthenticatedPostValid(self):
        """
        Test for authenticated user submitting valid data to edit observation using POST method.
        """

        response = self.client.post(
            reverse(
                "editObservation",
                kwargs={
                    "petitionId": self.monitoring_with_user.id,
                    "observationId": self.observation.id,
                },
            ),
            data={
                "description": "Observación editada",
                "date": "2024-04-01",
                "time": "12:00:00",
            },
        )
        self.assertEqual(response.status_code, 302)  # Redirect after successful POST

        # Reload the observation from the database
        updated_observation = Observation.objects.get(id=self.observation.id)
        self.assertEqual(updated_observation.description, "Observación editada")

    def testEditObservationPermission(self):
        """
        Test for user without correct permissions accessing edit observation view.
        """

        response = self.client.get(
            reverse(
                "editObservation",
                kwargs={
                    "petitionId": self.monitoring_with_user.id,
                    "observationId": self.observation.id,
                },
            )
        )
        self.assertEqual(
            response.status_code, 200
        )  # Forbidden without correct permissions

    def testEditObservationAuthenticatedPostInvalid(self):
        """
        Test for authenticated user submitting invalid data to edit observation using POST method.
        """
        response = self.client.post(
            reverse(
                "editObservation",
                kwargs={
                    "petitionId": self.monitoring_with_user.id,
                    "observationId": self.observation.id,
                },
            ),
            data={},
        )
        self.assertEqual(
            response.status_code, 200
        )  # Stay on the same page after invalid POST
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertTrue('description' in form.errors)
        self.assertEqual(form.errors['description'], ["Este campo es obligatorio."])

        

    def testEditObservationUnauthenticated(self):
        """
        Test for unauthenticated user accessing edit observation view.
        """

        self.client.logout()
        response = self.client.get(
            reverse(
                "editObservation",
                kwargs={
                    "petitionId": self.monitoring_with_user.id,
                    "observationId": self.observation.id,
                },
            )
        )
        self.assertEqual(response.status_code, 302)  # Redirect to login page
