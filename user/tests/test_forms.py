"""Django tests for forms in user login and sign up functionality"""
from django.test import TransactionTestCase
from user.forms import RegisterForm

class TestForms(TransactionTestCase):
    """Django test class for forms in user login and sign up functionality"""
    def test_registerform_validdata(self):

        form = RegisterForm(data={
            'username': 'John',
            'first_name' : 'John',
            'last_name' : 'Dwyer',
            'email' : 'jdwyer@ncsu.edu',
            'password1' : 'jd45678',
            'phone_number' : 987657890,
        })
        self.assertTrue(form.is_valid())
