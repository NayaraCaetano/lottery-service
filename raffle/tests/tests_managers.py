import datetime

from django.test import TestCase

from raffle.models import RaffleExecution


class RaffleExecutionManagerTest(TestCase):

    def test_create_from_raffle_param_list_validation(self):
        with self.assertRaises(RuntimeError):
            RaffleExecution.objects.create_from_raffle(items='not a list')

    def test_create_from_raffle_create_new_execution(self):
        items = ['a', 'b', 'c', 'd', 'e']
        obj = RaffleExecution.objects.create_from_raffle(items=items)
        self.assertIsNotNone(obj)
        self.assertEqual(obj.items, items)
        self.assertIn(obj.result, items)
        self.assertTrue(isinstance(obj.executed_at, datetime.datetime))
