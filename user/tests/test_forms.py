"""Django tests for forms in user login and sign up functionality"""

from django.test import TransactionTestCase
from django.contrib.auth.models import User
from user.forms import RegisterForm

class TestForms(TransactionTestCase):
    """Django test class for forms in user login and sign up functionality"""

    def setUp(self):
        """Set up test environment"""
        User.objects.create_user(username='existinguser', email='existing@example.com', password='password123')

    def test_registerform_validdata(self):
        """Tests for Registration Validation with valid data"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'password2': 'jd45678',
            'phone_number': '9876578901',
        })
        self.assertTrue(form.is_valid())

    def test_registerform_missing_username(self):
        """Test invalid registration form with missing username"""
        form = RegisterForm(data={
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'password2': 'jd45678',
            'phone_number': '9876578901',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_registerform_missing_email(self):
        """Test invalid registration form with missing email"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'password1': 'jd45678',
            'password2': 'jd45678',
            'phone_number': '9876578901',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_registerform_missing_password(self):
        """Test invalid registration form with missing password"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'phone_number': '9876578901',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors)

    def test_registerform_mismatched_passwords(self):
        """Test invalid registration form with mismatched passwords"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'password2': 'jd45679',
            'phone_number': '9876578901',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_registerform_short_password(self):
        """Test invalid registration form with short password"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45',
            'password2': 'jd45',
            'phone_number': '9876578901',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_registerform_common_password(self):
        """Test invalid registration form with common password"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'password',
            'password2': 'password',
            'phone_number': '9876578901',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_registerform_invalid_username(self):
        """Test invalid registration form with username containing special characters"""
        form = RegisterForm(data={
            'username': 'John@123',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'password2': 'jd45678',
            'phone_number': '9876578901',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_registerform_invalid_email(self):
        """Test invalid registration form with invalid email format"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu',
            'password1': 'jd45678',
            'password2': 'jd45678',
            'phone_number': '9876578901',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_registerform_existing_username(self):
        """Test invalid registration form with existing username"""
        form = RegisterForm(data={
            'username': 'existinguser',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'new@example.com',
            'password1': 'jd45678',
            'password2': 'jd45678',
            'phone_number': '9876578901',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_registerform_existing_email(self):
        """Test invalid registration form with existing email"""
        form = RegisterForm(data={
            'username': 'newuser',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'existing@example.com',
            'password1': 'jd45678',
            'password2': 'jd45678',
            'phone_number': '9876578901',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_registerform_minimum_fields(self):
        """Test valid registration form with minimum required fields"""
        form = RegisterForm(data={
            'username': 'John',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'password2': 'jd45678',
        })
        self.assertTrue(form.is_valid())

    def test_registerform_all_fields(self):
        """Test valid registration form with all fields filled"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'password2': 'jd45678',
            'phone_number': '9876578901',
        })
        self.assertTrue(form.is_valid())

    def test_registerform_invalid_phone(self):
        """Test invalid registration form with phone number containing letters"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'password2': 'jd45678',
            'phone_number': '98765abc01',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors)

    def test_registerform_invalid_first_name(self):
        """Test invalid registration form with first name containing numbers"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John123',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'password2': 'jd45678',
            'phone_number': '9876578901',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)

    def test_registerform_invalid_last_name(self):
        """Test invalid registration form with last name containing special characters"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Dwyer@',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'password2': 'jd45678',
            'phone_number': '9876578901',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors)

    def test_registerform_max_length_username(self):
        """Test valid registration form with maximum length username"""
        form = RegisterForm(data={
            'username': 'a' * 150,
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'password2': 'jd45678',
        })
        self.assertTrue(form.is_valid())

    def test_registerform_max_length_email(self):
        """Test valid registration form with maximum length email"""
        form = RegisterForm(data={
            'username': 'John',
            'email': 'a' * 242 + '@example.com',
            'password1': 'jd45678',
            'password2': 'jd45678',
        })
        self.assertTrue(form.is_valid())

    def test_registerform_password_same_as_username(self):
        """Test invalid registration form with password same as username"""
        form = RegisterForm(data={
            'username': 'johndwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'johndwyer',
            'password2': 'johndwyer',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)