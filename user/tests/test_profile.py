<<<<<<< HEAD
=======
"""Django tests for ProfileForm and user_profile view"""
>>>>>>> 6958b7e1dec9ede84c61dfc22d7ab2100b41f9c0
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from user.forms import ProfileForm
from user.models import Profile

class TestProfileForm(TestCase):
<<<<<<< HEAD
    def test_profileform_validdata(self):
=======
    """Django test class for ProfileForm"""

    def test_profileform_validdata(self):
        """Tests for Profile Form Validation with valid data"""
>>>>>>> 6958b7e1dec9ede84c61dfc22d7ab2100b41f9c0
        form = ProfileForm(data={
            'travel_preferences': 'Beach, Mountains',
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertTrue(form.is_valid())

    def test_profileform_invaliddata(self):
<<<<<<< HEAD
        form = ProfileForm(data={
            'travel_preferences': '',
=======
        """Tests for Profile Form Validation with invalid data"""
        form = ProfileForm(data={
            'travel_preferences': '',  # Required field
>>>>>>> 6958b7e1dec9ede84c61dfc22d7ab2100b41f9c0
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('travel_preferences', form.errors)

class TestUserProfileView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.profile_url = reverse('user_profile')

    def test_profile_get(self):
<<<<<<< HEAD
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ProfileForm)

    def test_profile_post_valid(self):
=======
        """Tests for GET request to user_profile view"""
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'user/profile.html')
        self.assertIsInstance(response.context['form'], ProfileForm)

    def test_profile_post_valid(self):
        """Tests for POST request to user_profile view with valid data"""
>>>>>>> 6958b7e1dec9ede84c61dfc22d7ab2100b41f9c0
        response = self.client.post(self.profile_url, {
            'travel_preferences': 'Beach, Mountains',
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
<<<<<<< HEAD
        self.assertRedirects(response, reverse('index'))  # Adjust the redirect URL as needed

        profile = Profile.objects.filter(user=self.user).first()
        self.assertIsNotNone(profile)
=======
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

        # Check if profile was updated
        profile = Profile.objects.get(user=self.user)
>>>>>>> 6958b7e1dec9ede84c61dfc22d7ab2100b41f9c0
        self.assertEqual(profile.travel_preferences, 'Beach, Mountains')
        self.assertEqual(profile.likes, 'Reading, Hiking')
        self.assertFalse(profile.is_smoker)

    def test_profile_post_invalid(self):
<<<<<<< HEAD
        response = self.client.post(self.profile_url, {
            'travel_preferences': '',
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ProfileForm)
        self.assertFalse(response.context['form'].is_valid())
=======
        """Tests for POST request to user_profile view with invalid data"""
        response = self.client.post(self.profile_url, {
            'travel_preferences': '',  # Required field
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'user/profile.html')
        self.assertIsInstance(response.context['form'], ProfileForm)
        self.assertFalse(response.context['form'].is_valid())
        
>>>>>>> 6958b7e1dec9ede84c61dfc22d7ab2100b41f9c0
