import secrets

from django.db import models


class RaffleExecutionManager(models.Manager):
    """
    Manager for Raffle Executions
    """

    def create_from_raffle(self, items):
        """
        :param items: list
        :return: RaffleExecution object
        """
        if not isinstance(items, list):
            raise RuntimeError('The items params must be a list')
        result = secrets.choice(items)
        return self.create(items=items, result=result)
