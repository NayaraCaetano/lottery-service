from django.test import TestCase
from model_mommy import mommy
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIClient

from raffle.models import RaffleExecution


class RaffleListCreateAPIViewTest(TestCase):
    url = reverse_lazy('raffles')

    def setUp(self):
        self.client = APIClient()

    def test_get_gest_raffles(self):
        mommy.make(RaffleExecution)
        mommy.make(RaffleExecution)
        mommy.make(RaffleExecution)
        mommy.make(RaffleExecution)
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(4, len(response.json()['results']))

    def test_execute_raffles(self):
        items = ['a', 'b', 'c', 'd', 'e']
        response = self.client.post(self.url, data={'items': items})
        self.assertEqual(201, response.status_code, response.json())
        self.assertIn(response.json()['result'], items, response.json())

    def test_execute_raffles_without_required_param(self):
        response = self.client.post(self.url, data={'items': []})
        self.assertEqual(400, response.status_code, response.json())
        self.assertIn('This field is required.', response.json()['items'])


class RaffleRetrieveAPIViewAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.obj = RaffleExecution.objects.create_from_raffle(['a', 'b', 'c', 'd', 'e'])
        self.url = reverse_lazy('raffle_details', kwargs={'pk': self.obj.pk})

    def test_get_raffle_detail(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.obj.id, response.json()['id'])
