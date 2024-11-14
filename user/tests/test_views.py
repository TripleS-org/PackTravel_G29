<<<<<<< HEAD
=======
"""File containing django view tests for various user functionality"""
>>>>>>> 6958b7e1dec9ede84c61dfc22d7ab2100b41f9c0
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse("index")
        self.register_url = reverse("register")
        self.logout_url = reverse("logout")
        self.login_url = reverse("login")
        self.test_user = User.objects.create_user(username="testuser", password="12345")

    def test_index(self):
<<<<<<< HEAD
=======
        """Tests for Client Index URL Validation"""
>>>>>>> 6958b7e1dec9ede84c61dfc22d7ab2100b41f9c0
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/home.html")

    def test_register(self):
<<<<<<< HEAD
=======
        """Tests for Client Register URL Validation"""
>>>>>>> 6958b7e1dec9ede84c61dfc22d7ab2100b41f9c0
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/register.html")

    def test_login(self):
<<<<<<< HEAD
=======
        """Tests for Client Login URL Validation"""
>>>>>>> 6958b7e1dec9ede84c61dfc22d7ab2100b41f9c0
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/login.html")

    def test_logout(self):
<<<<<<< HEAD
=======
        """Tests for Client Logout URL Validation"""
>>>>>>> 6958b7e1dec9ede84c61dfc22d7ab2100b41f9c0
        self.client.login(username="testuser", password="12345")
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))

<<<<<<< HEAD
    
    def test_login_invalid_credentials(self):
        response = self.client.post(self.login_url, {"username": "wronguser", "password": "wrongpass"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/login.html")
=======
    def test_login_redirect(self):
        """Tests for Client Login URL Validation"""
        response = self.client.post(self.login_url, {"username": "testuser", "password": "12345"})
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("index"))

    def test_login_invalid_credentials(self):
        """Tests for login with invalid credentials"""
        response = self.client.post(self.login_url, {"username": "wronguser", "password": "wrongpass"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/login.html")
>>>>>>> 6958b7e1dec9ede84c61dfc22d7ab2100b41f9c0
