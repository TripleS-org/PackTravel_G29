"""Django url tests for ride creation functionality"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from publish.views import publish_index, create_ride, show_ride, add_forum


class TestUrl(SimpleTestCase):
    """Class for testing urls in ride creation functionality"""
    def test_publish_index_resolves(self):
        url = reverse('publish')
        self.assertEquals(resolve(url).func, publish_index) # pylint: disable=deprecated-method

    def test_create_ride_resolves(self):
        url = reverse('create_ride')
        self.assertEquals(resolve(url).func, create_ride) # pylint: disable=deprecated-method

    def test_show_ride_resolves(self):
        url = reverse('showridepage', args=['078508ce-2efc-4316-8987-12b9551be5b4'])
        self.assertEquals(resolve(url).func, show_ride) # pylint: disable=deprecated-method

    def test_add_forum_resolves(self):
        url = reverse('addforum')
        self.assertEquals(resolve(url).func, add_forum) # pylint: disable=deprecated-method
