"""Django url tests for ride creation functionality"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from publish.views import publish_index, create_ride


class TestUrl(SimpleTestCase):
    """Class for testing urls in ride creation functionality"""
    def test_publish_index_resolved(self):
        url = reverse('publish')
        self.assertEquals(resolve(url).func, publish_index) # pylint: disable=deprecated-method

    def test_create_ride_resolved(self):
        url = reverse('create_ride')
        self.assertEquals(resolve(url).func, create_ride) # pylint: disable=deprecated-method
