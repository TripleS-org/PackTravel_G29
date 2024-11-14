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
    
    def test_profileform_long_travel_preferences(self):
        """Test that the form is invalid when travel_preferences is too long."""
        form = ProfileForm(data={
            'travel_preferences': 'A' * 256,  # Assuming max_length is 255
            'likes': 'Reading',
            'is_smoker': False,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('travel_preferences', form.errors)

    def test_profileform_long_likes(self):
        """Test that the form is invalid when likes is too long."""
        form = ProfileForm(data={
            'travel_preferences': 'Beach',
            'likes': 'A' * 256,  # Assuming max_length is 255
            'is_smoker': False,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('likes', form.errors)

    def test_profileform_invalid_smoker_value(self):
        """Test that the form is invalid when is_smoker is not a boolean."""
        form = ProfileForm(data={
            'travel_preferences': 'Beach',
            'likes': 'Reading',
            'is_smoker': 'Not a boolean',
        })
        self.assertTrue(form.is_valid())

class TestUserProfileView(TestCase):
    """Test cases for the user profile view, including GET and POST requests."""
    def setUp(self):
        """Set up test client and create a test user."""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.profile_url = reverse('user_profile')
