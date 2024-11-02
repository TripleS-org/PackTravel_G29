"""Django tests for forms in user login and sign up functionality"""

from django.test import TransactionTestCase
from django.contrib.auth.models import User
from user.forms import RegisterForm

class TestForms(TransactionTestCase):
    """Django test class for forms in user login and sign up functionality"""

    def setUp(self):
        """Set up test environment"""
        User.objects.create_user(username='existinguser', email='existing@example.com', password='password123')

    def test_registerform_valid_data(self):
        form = RegisterForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'first_name': 'Test',
            'last_name': 'User',
            'phone_number': '1234567890'
        })
        self.assertTrue(form.is_valid())

    def test_registerform_no_data(self):
        form = RegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)
