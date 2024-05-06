from django.test import TestCase, Client
from django.urls import reverse
from login.models import User
from django.contrib.auth.models import Group


class TestsIndexView(TestCase):
    """
    Test suite for index view.
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

    def testIndexViewAuthenticated(self):
        """
        Test index view with an authenticated user.
        """

        # Make a GET request to the view with an authenticated user
        response = self.client.get(reverse("index"))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the authenticated user is present in the view
        self.assertIn("user", response.context)
        self.assertEqual(response.context["user"], self.user)

    def testIndexViewUnauthenticated(self):
        """
        Test index view with an unauthenticated user.
        """

        # Create a new client without authentication
        unauthenticatedClient = Client()

        # Make a GET request to the view without authentication
        response = unauthenticatedClient.get(reverse("index"))

        # Check if the response status code is 302 (Redirect to login page)
        self.assertEqual(response.status_code, 302)

    def testIndexViewTemplateUsed(self):
        """
        Test index view template usage.
        """

        # Make a GET request to the view
        response = self.client.get(reverse("index"))

        # Check if the correct template is being used
        self.assertTemplateUsed(response, "index.html")

    def testIndexViewContains(self):
        """
        Test index view for expected content.
        """

        # Make a GET request to the view
        response = self.client.get(reverse("index"))

        # Check if the response context contains expected information
        self.assertContains(response, "Funcionalidades Destacadas")

    def testIndexViewContent(self):
        """
        Test index view content.
        """

        # Make a GET request to the view using the test client
        response = self.client.get(reverse("index"))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is being used
        self.assertTemplateUsed(response, "index.html")

        # Check if the response content is as expected
        self.assertContains(response, "Inicio - Tu Aplicación")

