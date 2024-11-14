from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from user.forms import ProfileForm
from user.models import Profile

class TestProfileForm(TestCase):
    def test_profileform_validdata(self):
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
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.profile_url = reverse('user_profile')

    def test_profile_get(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ProfileForm)

    def test_profile_post_valid(self):
        response = self.client.post(self.profile_url, {
            'travel_preferences': 'Beach, Mountains',
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertRedirects(response, reverse('index'))  # Adjust the redirect URL as needed

        profile = Profile.objects.filter(user=self.user).first()
        self.assertIsNotNone(profile)
        self.assertEqual(profile.travel_preferences, 'Beach, Mountains')
        self.assertEqual(profile.likes, 'Reading, Hiking')
        self.assertFalse(profile.is_smoker)

    def test_profile_post_invalid(self):
        response = self.client.post(self.profile_url, {
            'travel_preferences': '',
            'likes': 'Reading, Hiking',
            'is_smoker': False,
        })
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ProfileForm)
        self.assertFalse(response.context['form'].is_valid())
