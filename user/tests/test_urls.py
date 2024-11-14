"""Django url tests for user login and sign up functionality"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user.views import index, register, logout, login, user_profile
from django.contrib.auth import views as auth_views

class TestUrl(SimpleTestCase):
    """Django class to test urls for user login and sign up functionality"""

    def test_index_resolved(self):
        """Tests for Index URL resolution"""
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_register_resolved(self):
        """Tests for Register URL resolution"""
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)

    def test_login_resolved(self):
        """Tests for Login URL resolution"""
        url = reverse('login')
        self.assertEqual(resolve(url).func, login)

    def test_logout_resolved(self):
        """Tests for Logout URL resolution"""
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)

    def test_user_profile_resolved(self):
        """Tests for User Profile URL resolution"""
        url = reverse('user_profile')
        self.assertEqual(resolve(url).func, user_profile)

    def test_password_change_resolved(self):
        url = reverse('password_change')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordChangeView)

    def test_password_change_done_resolved(self):
        url = reverse('password_change_done')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordChangeDoneView)

    def test_password_reset_resolved(self):
        url = reverse('password_reset')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetView)

    def test_password_reset_done_resolved(self):
        url = reverse('password_reset_done')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetDoneView)

    def test_password_reset_confirm_resolved(self):
        url = reverse('password_reset_confirm', kwargs={'uidb64': 'test', 'token': 'test-token'})
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetConfirmView)

    def test_password_reset_complete_resolved(self):
        url = reverse('password_reset_complete')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetCompleteView)
