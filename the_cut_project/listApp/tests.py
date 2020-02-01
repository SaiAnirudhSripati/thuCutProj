from django.test import TestCase
from django.urls import reverse
# Create your tests here.



class ListAppTests(TestCase):
    def test_cat_list(self):
        url = reverse('list')
        response= self.client.get(url)
        self.assertEquals(response.status_code,200)
