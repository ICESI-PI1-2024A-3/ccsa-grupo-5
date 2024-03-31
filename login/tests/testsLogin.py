from django.test import TestCase, Client
from django.urls import reverse
from login.models import User
from django.contrib.auth.models import Group
from django.contrib.messages import get_messages


class testsLogin(TestCase):
    def setUp(self):
        # Crear un usuario para simular la autenticación
        Group.objects.get_or_create(name="Admin")
        self.user = User.objects.create(username="testuser", password="testpassword")
        group = Group.objects.get(name="Admin")
        self.user.groups.add(group)
        self.client = Client()
        self.client.force_login(self.user)

    def testLoginViewGet(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")
        self.assertIn("form", response.context)

    def testLoginViewPostValid(self):
        response = self.client.post(
            reverse("login"), {"username": "testuser", "password": "testpassword"}
        )
        self.assertEqual(response.status_code, 200)

    def testLoginViewPostInvalid(self):
        response = self.client.post(
            reverse("login"), {"username": "invalid", "password": "invalid"}
        )
        self.assertEqual(response.status_code, 200)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), "Acceso inválido. Por favor, inténtelo otra vez."
        )

    def testLoginViewAuthenticated(self):
        self.client.logout()
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def testLoginViewLogout(self):
        response = self.client.get(reverse("logoutSesion"))
        self.assertRedirects(response, reverse("login"))
