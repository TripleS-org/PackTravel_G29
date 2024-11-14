"""Django tests for forms in user login and sign up functionality"""
from django.test import TransactionTestCase
from user.forms import RegisterForm

class TestForms(TransactionTestCase):
    """Django test class for forms in user login and sign up functionality"""
    def test_registerform_validdata(self):
        """Tests for Registration Validation"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name' : 'John',
            'last_name' : 'Dwyer',
            'email' : 'jdwyer@ncsu.edu',
            'password1' : 'jd45678',
            'phone_number' : 987657890,
        })
        self.assertTrue(form.is_valid())
    def test_registerform_missing_username(self):
        """Test form validation when username is missing"""
        form = RegisterForm(data={
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'phone_number': 9876578901,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_registerform_invalid_email(self):
        """Test form validation with an invalid email"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'invalid_email',
            'password1': 'jd45678',
            'phone_number': 9876578901,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_registerform_short_password(self):
        """Test form validation with a short password"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'short',
            'phone_number': 9876578901,
        })
        self.assertTrue(form.is_valid())

    def test_registerform_invalid_phone_number(self):
        """Test form validation with an invalid phone number"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'phone_number': 123,  # Too short
        })
        self.assertTrue(form.is_valid())

    def test_registerform_duplicate_username(self):
        """Test form validation with a duplicate username"""
        # First, create a user with the username 'John'
        RegisterForm(data={
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'password1': 'password123',
            'phone_number': 9876543210,
        }).save()

        # Now try to create another user with the same username
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'phone_number': 9876578901,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_registerform_empty_form(self):
        """Test form validation with an empty form"""
        form = RegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)  # All fields should have errors

    def test_registerform_whitespace_username(self):
        """Test form validation with whitespace username"""
        form = RegisterForm(data={
            'username': '   ',
            'first_name': 'John',
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'phone_number': 9876578901,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_registerform_long_first_name(self):
        """Test form validation with a very long first name"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'J' * 101,  # 101 characters
            'last_name': 'Dwyer',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'phone_number': 9876578901,
        })
        self.assertTrue(form.is_valid())

    def test_registerform_special_chars_in_name(self):
        """Test form validation with special characters in the name"""
        form = RegisterForm(data={
            'username': 'John',
            'first_name': 'John@123',
            'last_name': 'Dwyer!',
            'email': 'jdwyer@ncsu.edu',
            'password1': 'jd45678',
            'phone_number': 9876578901,
        })
        self.assertTrue(form.is_valid())
