from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

"""Test cases for user views, including registration, login, logout, and index page functionality."""

class TestViews(TestCase):
    """Test case class for testing views like index, register, login, and logout."""
    def setUp(self):
        self.client = Client()
        self.index_url = reverse("index")
        self.register_url = reverse("register")
        self.logout_url = reverse("logout")
        self.login_url = reverse("login")
        self.test_user = User.objects.create_user(username="testuser", password="12345")

    def test_index(self):
        """Test the index page loads successfully and uses the correct template."""
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/home.html")

    def test_register(self):
        """Test the register page loads successfully and uses the correct template."""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/register.html")

    def test_login(self):
        """Test the login page loads successfully and uses the correct template."""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/login.html")

    def test_logout(self):
        """Test the logout page loads successfully and uses the correct template."""
        self.client.login(username="testuser", password="12345")
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))


    def test_login_invalid_credentials(self):
        """Test the login page loads successfully and uses the correct template."""
        response = self.client.post(self.login_url, 
        {"username": "wronguser", "password": "wrongpass"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/login.html")
