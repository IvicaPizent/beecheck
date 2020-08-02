from django.test import TestCase, Client
from django.urls import reverse

from beecheck.models import Location
from beecheck.views import index

class IndexTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.client = Client()

		number_of_locations = 10

		for location_id in range(number_of_locations):
			Location.objects.create(location_name = f'Location {location_id}')

	def test_index_view_url_exists_at_desired_location(self):
		response = self.client.get('/beecheck/')
		self.assertEqual(response.status_code, 200)

	def test_index_view_url_accessible_by_name(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)

	def test_index_view_uses_correct_template(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')

	def test_index_view_lists_all_locations(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertTrue(len(response.context['loc']) == 10)

	def test_index_view_orders_by_location_name(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(list(response.context['loc']), list(Location.objects.order_by('location_name')))


