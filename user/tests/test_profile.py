"""Django tests for ProfileForm and user_profile view"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from user.forms import ProfileForm
from user.models import Profile

class TestProfileForm(TestCase):
    """Django test class for ProfileForm"""

    def test_profileform_validdata(self):
        """Tests for Profile Form Validation with valid data"""
        form = ProfileForm(data={
            'travel_preferences': 'Beach, Mountains',
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertTrue(form.is_valid())

    def test_profileform_invaliddata(self):
        """Tests for Profile Form Validation with invalid data"""
        form = ProfileForm(data={
            'travel_preferences': '',  # Required field
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('travel_preferences', form.errors)

class TestUserProfileView(TestCase):
    """Django test class for user_profile view"""

    def setUp(self):
        """Set up test environment"""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.profile_url = reverse('user_profile')

    def test_profile_get(self):
        """Tests for GET request to user_profile view"""
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile.html')
        self.assertIsInstance(response.context['form'], ProfileForm)

    def test_profile_post_valid(self):
        """Tests for POST request to user_profile view with valid data"""
        response = self.client.post(self.profile_url, {
            'travel_preferences': 'Beach, Mountains',
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

        # Check if profile was updated
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.travel_preferences, 'Beach, Mountains')
        self.assertEqual(profile.likes, 'Reading, Hiking')
        self.assertFalse(profile.is_smoker)

    def test_profile_post_invalid(self):
        """Tests for POST request to user_profile view with invalid data"""
        response = self.client.post(self.profile_url, {
            'travel_preferences': '',  # Required field
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile.html')
        self.assertIsInstance(response.context['form'], ProfileForm)
        self.assertFalse(response.context['form'].is_valid())

    def test_profile_unauthenticated(self):
        """Tests for unauthenticated access to user_profile view"""
        self.client.logout()
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('login')}?next={self.profile_url}")