from django.test import TestCase
from urllib.parse import urlencode
from django.urls import reverse

class Weather(TestCase):
	def test_search(self):
		data = urlencode({'city': 'London'})
		response = self.client.post(reverse("weather_report"), data, content_type="application/x-www-form-urlencoded")
		self.assertEqual(response.status_code, 200)
# Create your tests here.
