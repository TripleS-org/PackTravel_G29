"""File containing django view tests for ride creation functionality"""
from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    """Test class to test Django views for ride creation functionality"""
    def setUp(self):
        self.client = Client()
        self.publish_url = reverse("publish")
        self.create_ride_url = reverse("create_ride")
        self.show_ride_url = reverse("showridepage", args=["078508ce-2efc-4316-8987-12b9551be5b4"])
        self.add_forum_url = reverse("addforum")

    def test_publish_for_logged_out_user(self):
        response = self.client.get(self.publish_url)
        # 302 - redirects to index when user is not logged in
        self.assertEquals(response.status_code, 302) # pylint: disable=deprecated-method
        self.assertRedirects(response, "/index/")

    def test_publish_for_logged_in_user(self):
        session = self.client.session
        session["username"] = "test"
        session.save()
        response = self.client.get(self.publish_url)
        # go to publish page if session variable is set
        self.assertEquals(response.status_code, 200) # pylint: disable=deprecated-method
        self.assertTemplateUsed(response, "publish/publish.html")

    def test_ride_creation(self):
        session = self.client.session
        session["username"] = "django-test"
        session.save()
        response = self.client.post(self.create_ride_url, {
            "source": "Raleigh, NC",
            "destination": "New York, NY",
            "ride_type": "Personal",
            "capacity": 5,
            "date": "2023-12-31",
            "hour": "11",
            "minute": "00",
            "ampm": "am",
            "info": "Dummy data"
        })

        self.assertEquals(response.status_code, 200) # pylint: disable=deprecated-method
        self.assertTemplateUsed(response, "publish/publish.html")
