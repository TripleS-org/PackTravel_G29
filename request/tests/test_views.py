"""File containing django view tests for ride management functionality"""
from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    """Test class to test Django views for ride creation functionality"""
    def setUp(self):
        self.client = Client()
        self.requested_rides_url = reverse("requests")
        self.cancel_ride_url = reverse("cancel_ride", args=["078508ce-2efc-4316-8987-12b9551be5b4"])
        self.cancel_accepted_requests_url = reverse("cancel_accepted_request", args=["078508ce-2efc-4316-8987-12b9551be5b4", "test"])
        self.accept_request_url = reverse("accept_request", args=["078508ce-2efc-4316-8987-12b9551be5b4", "test"])
        self.reject_request_url = reverse("reject_request", args=["078508ce-2efc-4316-8987-12b9551be5b4", "test"])
        self.delete_ride_url = reverse("delete_ride", args=["078508ce-2efc-4316-8987-12b9551be5b4"])

    def test_requested_rides(self):
        """Tests for ride requested"""
        session = self.client.session
        session["username"] = "test"
        session.save()
        response = self.client.get(self.requested_rides_url)
        self.assertEqual(response.status_code, 200) # pylint: disable=deprecated-method
        self.assertTemplateUsed(response, "requests/requests.html")

    def test_cancel_ride_logged_in_user(self):
        """Tests for ride canceled for logged in user"""
        session = self.client.session
        session["username"] = "test"
        session.save()
        response = self.client.get(self.cancel_ride_url)
        # go to requests page
        self.assertEqual(response.status_code, 302) # pylint: disable=deprecated-method
        self.assertRedirects(response, "/requests/")

    def test_accept_ride_request(self):
        """Tests for ride accepted"""
        session = self.client.session
        session["username"] = "test"
        session.save()
        response = self.client.get(self.accept_request_url)
        # go to requests page
        self.assertEqual(response.status_code, 302) # pylint: disable=deprecated-method
        self.assertRedirects(response, "/requests/")

    def test_reject_ride_request(self):
        """Tests for ride rejected"""
        session = self.client.session
        session["username"] = "test"
        session.save()
        response = self.client.get(self.reject_request_url)
        # go to requests page
        self.assertEqual(response.status_code, 302) # pylint: disable=deprecated-method
        self.assertRedirects(response, "/requests/")

    def test_cancel_accepted_ride(self):
        """Tests for accepted ride cancellation"""
        session = self.client.session
        session["username"] = "test"
        session.save()
        response = self.client.get(self.cancel_accepted_requests_url)
        # go to requests page
        self.assertEqual(response.status_code, 302) # pylint: disable=deprecated-method
        self.assertRedirects(response, "/requests/")

    def test_delete_ride(self):
        """Tests for ride deleted"""
        session = self.client.session
        session["username"] = "test"
        session.save()
        response = self.client.get(self.delete_ride_url)
        # go to requests page
        self.assertEqual(response.status_code, 302) # pylint: disable=deprecated-method
        self.assertRedirects(response, "/requests/")
