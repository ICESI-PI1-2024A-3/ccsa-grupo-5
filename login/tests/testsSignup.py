from django.test import TestCase, Client
from django.urls import reverse
from login.forms.userForm import UserForm
from login.models import User
from django.contrib.auth.models import Group
from django.contrib.messages import get_messages


class testSignup(TestCase):
    """
    Test suite for the signup view.
    """

    def setUp(self):
        """
        Set up data for each test.
        """
        self.signupUrl = reverse("signup")
        Group.objects.get_or_create(name="Admin")
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@gmail.com",
            password="testpassword",
            first_name="Test",
            last_name="User",
        )
        group = Group.objects.get(name="Admin")
        self.user.groups.add(group)
        self.client = Client()
        self.client.force_login(self.user)

    def testSignupFormInvalid(self):
        """
        Test invalid user creation form.
        """
        form = UserForm(data={})
        self.assertFalse(form.is_valid())

    def testSignupViewPost(self):
        """
        Test POST request to signup view.
        """
        response = self.client.post(
            self.signupUrl,
            {
                "first_name": "Test",
                "last_name": "User",
                "email": "testuser@gmail.com",
                "username": "testuser",
                "password1": "testpassword123",
                "password2": "testpassword123",
                "roles": "leader",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "signup.html")

    def testSignupViewGet(self):
        """
        Test GET request to signup view.
        """
        response = self.client.get(self.signupUrl)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "signup.html")

    def testUserCreation(self):
        """
        Test user creation.
        """
        self.client.post(
            self.signupUrl,
            {
                "first_name": "Test",
                "last_name": "User",
                "email": "testuser@gmail.com",
                "username": "testuser",
                "password1": "testpassword123",
                "password2": "testpassword123",
                "roles": "leader",
            },
        )
        user = User.objects.filter(username="testuser").first()
        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")
        self.assertEqual(user.email, "testuser@gmail.com")
