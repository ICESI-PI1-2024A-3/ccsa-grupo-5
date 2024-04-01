from django.test import TestCase, Client
from django.urls import reverse
from login.models import User
from django.contrib.auth.models import Group


class testsIndex(TestCase):
    """
    Test suite for the index view.
    """

    def setUp(self):
        """
        Set up data for each test.
        """
        Group.objects.get_or_create(name="Admin")
        self.user = User.objects.create(username="testuser", password="testpassword")
        group = Group.objects.get(name="Admin")
        self.user.groups.add(group)
        self.client = Client()
        self.client.force_login(self.user)

    def testIndexViewAuthenticated(self):
        """
        Test access to index view with an authenticated user.
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("user", response.context)
        self.assertEqual(response.context["user"], self.user)

    def testIndexViewUnauthenticated(self):
        """
        Test access to index view without authentication.
        """
        unauthenticated_client = Client()
        response = unauthenticated_client.get(reverse("index"))
        self.assertEqual(response.status_code, 302)

    def testIndexViewTemplateUsed(self):
        """
        Test template used for index view.
        """
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")

    def testIndexContains(self):
        """
        Test content of index view.
        """
        response = self.client.get(reverse("index"))
        self.assertContains(response, "Crear usuario")
        self.assertContains(response, "Crear Solicitudes")

    def testIndexView(self):
        """
        Test index view content.
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "<h1>Bienvenido a Tu Aplicación</h1>")
        self.assertContains(
            response,
            "<p>Una aplicación para gestionar solicitudes de contrato de manera eficiente.</p>",
        )
