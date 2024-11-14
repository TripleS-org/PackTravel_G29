from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from user.forms import ProfileForm
from user.models import Profile

"""Test cases for user profile functionality including form validation and view behavior."""

class TestProfileForm(TestCase):
    """Test cases for the Profile form."""

    def test_profileform_validdata(self):
        """Test that the form is valid when given valid data."""

        form = ProfileForm(data={
            'travel_preferences': 'Beach, Mountains',
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertTrue(form.is_valid())

    def test_profileform_invaliddata(self):
        form = ProfileForm(data={
            'travel_preferences': '',
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('travel_preferences', form.errors)

class TestUserProfileView(TestCase):
    """Test cases for the user profile view, including GET and POST requests."""
    def setUp(self):
        """Set up test client and create a test user."""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.profile_url = reverse('user_profile')
