"""Django url tests for user login and sign up functionality"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user.views import index, register, logout, login

class TestUrl(SimpleTestCase):
    """Django class to test urls for user login and sign up functionality"""

    def test_index_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index) # pylint: disable=deprecated-method

    def test_register_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register) # pylint: disable=deprecated-method

    def test_login_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login) # pylint: disable=deprecated-method

    def test_logout_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout) # pylint: disable=deprecated-method
