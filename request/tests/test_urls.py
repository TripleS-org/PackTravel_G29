"""Django url tests for ride management functionality"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from request.views import requested_rides, cancel_ride, cancel_accepted_ride, accept_request, reject_request, delete_ride


class TestUrl(SimpleTestCase):
    """Class for testing urls in ride management functionality"""
    def test_requested_ride_resolves(self):
        url = reverse('requests')
        self.assertEquals(resolve(url).func, requested_rides) # pylint: disable=deprecated-method

    def test_cancel_ride_resolves(self):
        url = reverse('cancel_ride', args=['078508ce-2efc-4316-8987-12b9551be5b4'])
        self.assertEquals(resolve(url).func, cancel_ride) # pylint: disable=deprecated-method

    def test_cancel_accepted_ride_resolves(self):
        url = reverse('cancel_accepted_request', args=['078508ce-2efc-4316-8987-12b9551be5b4', 'test'])
        self.assertEquals(resolve(url).func, cancel_accepted_ride) # pylint: disable=deprecated-method

    def test_accept_request_resolves(self):
        url = reverse('accept_request', args=['078508ce-2efc-4316-8987-12b9551be5b4', 'test'])
        self.assertEquals(resolve(url).func, accept_request) # pylint: disable=deprecated-method

    def test_reject_request_resolves(self):
        url = reverse('reject_request', args=['078508ce-2efc-4316-8987-12b9551be5b4', 'test'])
        self.assertEquals(resolve(url).func, reject_request) # pylint: disable=deprecated-method

    def test_delete_ride_resolves(self):
        url = reverse('delete_ride', args=['078508ce-2efc-4316-8987-12b9551be5b4'])
        self.assertEquals(resolve(url).func, delete_ride) # pylint: disable=deprecated-method
