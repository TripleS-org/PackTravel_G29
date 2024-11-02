"""Django url tests for user login and sign up functionality"""

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user.views import (
    index, register, logout, login, profile, password_reset, password_reset_confirm,
    password_change, user_detail, user_list, user_update, user_delete,
    custom_404, custom_500, terms_of_service, privacy_policy, about_us, contact_us,
    faq, sitemap
)

class TestUrl(SimpleTestCase):
    """Django class to test urls for user login and sign up functionality"""

    def test_index_resolved(self):
        """Tests for Index URL resolution"""
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_register_resolved(self):
        """Tests for Register URL resolution"""
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_login_resolved(self):
        """Tests for Login URL resolution"""
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_logout_resolved(self):
        """Tests for Logout URL resolution"""
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout)

    def test_profile_resolved(self):
        """Tests for Profile URL resolution"""
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_password_reset_resolved(self):
        """Tests for Password Reset URL resolution"""
        url = reverse('password_reset')
        self.assertEquals(resolve(url).func, password_reset)

    def test_password_reset_confirm_resolved(self):
        """Tests for Password Reset Confirm URL resolution"""
        url = reverse('password_reset_confirm', args=['uidb64', 'token'])
        self.assertEquals(resolve(url).func, password_reset_confirm)

    def test_password_change_resolved(self):
        """Tests for Password Change URL resolution"""
        url = reverse('password_change')
        self.assertEquals(resolve(url).func, password_change)

    def test_user_detail_resolved(self):
        """Tests for User Detail URL resolution"""
        url = reverse('user_detail', args=[1])
        self.assertEquals(resolve(url).func, user_detail)

    def test_user_list_resolved(self):
        """Tests for User List URL resolution"""
        url = reverse('user_list')
        self.assertEquals(resolve(url).func, user_list)

    def test_user_update_resolved(self):
        """Tests for User Update URL resolution"""
        url = reverse('user_update', args=[1])
        self.assertEquals(resolve(url).func, user_update)

    def test_user_delete_resolved(self):
        """Tests for User Delete URL resolution"""
        url = reverse('user_delete', args=[1])
        self.assertEquals(resolve(url).func, user_delete)

    def test_custom_404_resolved(self):
        """Tests for Custom 404 Error Page URL resolution"""
        url = reverse('custom_404')
        self.assertEquals(resolve(url).func, custom_404)

    def test_custom_500_resolved(self):
        """Tests for Custom 500 Error Page URL resolution"""
        url = reverse('custom_500')
        self.assertEquals(resolve(url).func, custom_500)

    def test_terms_of_service_resolved(self):
        """Tests for Terms of Service URL resolution"""
        url = reverse('terms_of_service')
        self.assertEquals(resolve(url).func, terms_of_service)

    def test_privacy_policy_resolved(self):
        """Tests for Privacy Policy URL resolution"""
        url = reverse('privacy_policy')
        self.assertEquals(resolve(url).func, privacy_policy)

    def test_about_us_resolved(self):
        """Tests for About Us URL resolution"""
        url = reverse('about_us')
        self.assertEquals(resolve(url).func, about_us)

    def test_contact_us_resolved(self):
        """Tests for Contact Us URL resolution"""
        url = reverse('contact_us')
        self.assertEquals(resolve(url).func, contact_us)

    def test_faq_resolved(self):
        """Tests for FAQ URL resolution"""
        url = reverse('faq')
        self.assertEquals(resolve(url).func, faq)

    def test_sitemap_resolved(self):
        """Tests for Sitemap URL resolution"""
        url = reverse('sitemap')
        self.assertEquals(resolve(url).func, sitemap)