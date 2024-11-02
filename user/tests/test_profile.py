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
            'travel_preferences': '', # Required field
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('travel_preferences', form.errors)

    def test_profileform_missing_likes(self):
        """Test ProfileForm with empty likes"""
        form = ProfileForm(data={
            'travel_preferences': 'Beach, Mountains',
            'likes': '',
            'is_smoker': False,
        })
        self.assertTrue(form.is_valid())

    def test_profileform_invalid_smoker(self):
        """Test ProfileForm with invalid is_smoker value"""
        form = ProfileForm(data={
            'travel_preferences': 'Beach, Mountains',
            'likes': 'Reading, Hiking',
            'is_smoker': 'Invalid',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('is_smoker', form.errors)

    def test_profileform_max_length_preferences(self):
        """Test ProfileForm with maximum length travel preferences"""
        max_length = ProfileForm.base_fields['travel_preferences'].max_length
        form = ProfileForm(data={
            'travel_preferences': 'a' * max_length,
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertTrue(form.is_valid())

    def test_profileform_max_length_likes(self):
        """Test ProfileForm with maximum length likes"""
        max_length = ProfileForm.base_fields['likes'].max_length
        form = ProfileForm(data={
            'travel_preferences': 'Beach, Mountains',
            'likes': 'a' * max_length,
            'is_smoker': False,
        })
        self.assertTrue(form.is_valid())

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
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.travel_preferences, 'Beach, Mountains')
        self.assertEqual(profile.likes, 'Reading, Hiking')
        self.assertFalse(profile.is_smoker)

    def test_profile_post_invalid(self):
        """Tests for POST request to user_profile view with invalid data"""
        response = self.client.post(self.profile_url, {
            'travel_preferences': '', # Required field
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

    def test_profile_post_update_existing(self):
        """Test user_profile view POST request updating existing profile"""
        Profile.objects.create(user=self.user, travel_preferences='City', likes='Shopping', is_smoker=True)
        response = self.client.post(self.profile_url, {
            'travel_preferences': 'Beach, Mountains',
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertEqual(response.status_code, 302)
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.travel_preferences, 'Beach, Mountains')
        self.assertEqual(profile.likes, 'Reading, Hiking')
        self.assertFalse(profile.is_smoker)

    def test_profile_post_create_new(self):
        """Test user_profile view POST request creating new profile"""
        self.assertFalse(Profile.objects.filter(user=self.user).exists())
        response = self.client.post(self.profile_url, {
            'travel_preferences': 'Beach, Mountains',
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_profile_get_existing_profile(self):
        """Test user_profile view GET request with existing profile"""
        Profile.objects.create(user=self.user, travel_preferences='City', likes='Shopping', is_smoker=True)
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile.html')
        form = response.context['form']
        self.assertEqual(form.initial['travel_preferences'], 'City')
        self.assertEqual(form.initial['likes'], 'Shopping')
        self.assertTrue(form.initial['is_smoker'])

    def test_profile_get_no_existing_profile(self):
        """Test user_profile view GET request with no existing profile"""
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile.html')
        form = response.context['form']
        self.assertFalse(form.is_bound)

    def test_profile_post_empty_likes(self):
        """Test user_profile view POST request with empty likes"""
        response = self.client.post(self.profile_url, {
            'travel_preferences': 'Beach, Mountains',
            'likes': '',
            'is_smoker': False,
        })
        self.assertEqual(response.status_code, 302)
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.likes, '')

    def test_profile_post_long_preferences(self):
        """Test user_profile view POST request with long travel preferences"""
        max_length = ProfileForm.base_fields['travel_preferences'].max_length
        long_preferences = 'a' * (max_length + 1)
        response = self.client.post(self.profile_url, {
            'travel_preferences': long_preferences,
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())

    def test_profile_post_long_likes(self):
        """Test user_profile view POST request with long likes"""
        max_length = ProfileForm.base_fields['likes'].max_length
        long_likes = 'a' * (max_length + 1)
        response = self.client.post(self.profile_url, {
            'travel_preferences': 'Beach, Mountains',
            'likes': long_likes,
            'is_smoker': False,
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())

class TestProfileModel(TestCase):
    """Test class for Profile model"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_profile_creation(self):
        """Test Profile model creation with minimum required fields"""
        profile = Profile.objects.create(user=self.user, travel_preferences='Beach')
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.travel_preferences, 'Beach')
        self.assertEqual(profile.likes, '')
        self.assertFalse(profile.is_smoker)

    def test_profile_str_representation(self):
        """Test Profile model string representation"""
        profile = Profile.objects.create(user=self.user, travel_preferences='Beach')
        self.assertEqual(str(profile), f"{self.user.username}'s profile")

    def test_profile_default_values(self):
        """Test Profile model default values"""
        profile = Profile.objects.create(user=self.user, travel_preferences='Beach')
        self.assertEqual(profile.likes, '')
        self.assertFalse(profile.is_smoker)

    def test_profile_full_fields(self):
        """Test Profile model creation with all fields"""
        profile = Profile.objects.create(
            user=self.user,
            travel_preferences='Beach, Mountains',
            likes='Reading, Hiking',
            is_smoker=True
        )
        self.assertEqual(profile.travel_preferences, 'Beach, Mountains')
        self.assertEqual(profile.likes, 'Reading, Hiking')
        self.assertTrue(profile.is_smoker)