from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from raffle.models import RaffleExecution
from raffle.serializers import RaffleSerializer


class RaffleListCreateAPIView(ListCreateAPIView):
    serializer_class = RaffleSerializer
    queryset = RaffleExecution.objects.all()


class RaffleRetrieveAPIView(RetrieveAPIView):
    serializer_class = RaffleSerializer
    queryset = RaffleExecution.objects.all()
