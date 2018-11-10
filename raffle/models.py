from django.contrib.postgres.fields import ArrayField
from django.db import models

from raffle.managers import RaffleExecutionManager


class RaffleExecution(models.Model):
    items = ArrayField(models.CharField(max_length=255))
    executed_at = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=255)

    objects = RaffleExecutionManager()
