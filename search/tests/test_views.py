"""File containing django view tests for ride search functionality"""
from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    """Test class to test Django views for ride creation functionality"""
    def setUp(self):
        self.client = Client()
        self.search_url = reverse("search")
        self.request_ride_url = reverse("request_ride", args=["078508ce-2efc-4316-8987-12b9551be5b4"])

    def test_search_logged_out_user(self):
        """Tests for searching logged out user"""
        response = self.client.get(self.search_url)
        self.assertEquals(response.status_code, 302) # pylint: disable=deprecated-method
        self.assertRedirects(response, "/index/")

    def test_search_logged_in_user(self):
        """Tests for searching logged in user"""
        session = self.client.session
        session["username"] = "test"
        session.save()
        response = self.client.get(self.search_url)
        # go to requests page
        self.assertEquals(response.status_code, 200) # pylint: disable=deprecated-method
        self.assertTemplateUsed(response, "search/search.html")

    def test_request_ride(self):
        """Tests for requesting ride"""
        session = self.client.session
        session["username"] = "test"
        session.save()
        response = self.client.get(self.request_ride_url)
        # go to requests page
        self.assertEquals(response.status_code, 302) # pylint: disable=deprecated-method
        self.assertRedirects(response, "/requests/")
