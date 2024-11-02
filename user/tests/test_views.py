"""File containing django view tests for various user functionality"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):
    """Test class to test Django views for various user functionality"""

    def setUp(self):
        """Set up test environment"""
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.profile_url = reverse('profile')
        self.password_change_url = reverse('password_change')
        self.password_reset_url = reverse('password_reset')
        self.user = User.objects.create_user(username='testuser', password='12345')



        # Create a test user
        self.test_user = User.objects.create_user(username='testuser', email='testuser@example.com', password='12345')

    def test_index_authenticated(self):
        """Test index view for authenticated user"""
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/home.html")
        self.assertContains(response, "Welcome, testuser")

    def test_index_unauthenticated(self):
        """Test index view for unauthenticated user"""
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/home.html")
        self.assertNotContains(response, "Welcome, testuser")

    def test_register_get(self):
        """Test register view GET request"""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/register.html")

    def test_register_post_valid(self):
        """Test register view POST request with valid data"""
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_register_post_invalid(self):
        """Test register view POST request with invalid data"""
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'email': 'invalid_email',
            'password1': 'short',
            'password2': 'short'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/register.html")
        self.assertFalse(User.objects.filter(username='newuser').exists())

    def test_login_get(self):
        """Test login view GET request"""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/login.html")

    def test_login_post_valid(self):
        """Test login view POST request with valid credentials"""
        response = self.client.post(self.login_url, {
            "username": "testuser",
            "password": "12345"
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))

    def test_login_post_invalid(self):
        """Test login view POST request with invalid credentials"""
        response = self.client.post(self.login_url, {
            "username": "wronguser",
            "password": "wrongpass"
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/login.html")
        self.assertContains(response, "Please enter a correct username and password")

    def test_logout_authenticated(self):
        """Test logout view for authenticated user"""
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))

    def test_logout_unauthenticated(self):
        """Test logout view for unauthenticated user"""
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))

    def test_profile_get_authenticated(self):
        """Test profile view GET request for authenticated user"""
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/profile.html")

    def test_profile_get_unauthenticated(self):
        """Test profile view GET request for unauthenticated user"""
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('login')}?next={self.profile_url}")

    def test_profile_post_valid(self):
        """Test profile view POST request with valid data"""
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.profile_url, {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("profile"))
        updated_user = User.objects.get(username='testuser')
        self.assertEqual(updated_user.first_name, 'Test')
        self.assertEqual(updated_user.last_name, 'User')

    def test_profile_post_invalid(self):
        """Test profile view POST request with invalid data"""
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.profile_url, {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'invalid_email'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/profile.html")
        self.assertContains(response, "Enter a valid email address")

    def test_ride_creation(self):
        response = self.client.post(reverse('create_ride'), data)
        self.assertEquals(response.status_code, 201)  