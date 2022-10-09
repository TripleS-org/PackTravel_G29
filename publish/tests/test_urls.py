from django.test import SimpleTestCase
from django.urls import reverse, resolve
from publish.views import publish_index, display_ride,create_ride,add_route


class TestUrl(SimpleTestCase):

    def test_publish_index_resolved(self):
        url = reverse('publish')
        self.assertEquals(resolve(url).func, publish_index)

    def test_create_ride_resolved(self):
        url = reverse('create_ride')
        self.assertEquals(resolve(url).func, create_ride)

    # def test_login_resolved(self):
    #     url = reverse('display_ride')
    #     self.assertEquals(resolve(url).func, display_ride)

    def test_add_route_resolved(self):
        url = reverse('add_route')
        self.assertEquals(resolve(url).func, add_route)

