from django.test import TransactionTestCase
from user.forms import RegisterForm,LoginForm

class TestForms(TransactionTestCase):
     def test_registerForm_validData(self):

         form = RegisterForm(data={
                                'username': 'John',
                                'unityid' : 'ajohn6',
                                'first_name' : 'John',
                                'last_name' : 'Dwyer',
                                'email' : 'jdwyer@ncsu.edu',
                                'password1' : 'jd45678',
                                'phone_number' : 987657890,
                             })
         self.assertTrue(form.is_valid())