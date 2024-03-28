from django.test import TestCase, Client
from django.urls import reverse
from login.models import User


class TestsIndex(TestCase):
    def setUp(self):
        # Crear un usuario para simular la autenticación
        self.user = User.objects.create(username="testuser", password="testpassword")
        self.client = Client()
        self.client.force_login(self.user)

    def testIndexViewAuthenticated(self):
        # Hacer una solicitud GET a la vista con un usuario autenticado
        response = self.client.get(reverse("index"))

        # Verificar que la respuesta tenga el código 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar que el usuario autenticado está presente en la vista
        self.assertIn("user", response.context)
        self.assertEqual(response.context["user"], self.user)

    def testIndexViewUnauthenticated(self):
        # Crear un nuevo cliente sin autenticación
        unauthenticatedClient = Client()

        # Hacer una solicitud GET a la vista sin autenticación
        response = unauthenticatedClient.get(reverse("index"))

        # Verificar que la respuesta tenga el código 302 (Redirección a la página de inicio de sesión)
        self.assertEqual(response.status_code, 302)

    def testIndexViewTemplateUsed(self):
        # Hacer una solicitud GET a la vista
        response = self.client.get(reverse("index"))

        # Verificar que se está utilizando el template correcto
        self.assertTemplateUsed(response, "index.html")

    def testIndexContains(self):
        # Hacer una solicitud GET a la vista
        response = self.client.get(reverse("index"))

        # Verificar que el contexto de la respuesta contiene información esperada
        self.assertContains(response, "Crear usuario")
        self.assertContains(response, "Crear Solicitudes")

    def testIndexView(self):
        # Hacer una solicitud GET a la vista usando el cliente de prueba
        response = self.client.get(reverse("index"))

        # Verificar que la respuesta tenga el código 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar que la plantilla usada es la correcta
        self.assertTemplateUsed(response, "index.html")

        # Verificar que el contenido de la respuesta es el esperado
        self.assertContains(response, "<h1>Bienvenido a Tu Aplicación</h1>")
        self.assertContains(
            response,
            "<p>Una aplicación para gestionar solicitudes de contrato de manera eficiente.</p>",
        )
