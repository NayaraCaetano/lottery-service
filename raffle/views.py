from django_filters import rest_framework as filters

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from raffle.models import RaffleExecution
from raffle.serializers import RaffleSerializer


class RaffleFilter(filters.FilterSet):
    executed_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = RaffleExecution
        fields = ('result', 'executed_at')


class RaffleListCreateAPIView(ListCreateAPIView):
    filterset_class = RaffleFilter
    serializer_class = RaffleSerializer
    queryset = RaffleExecution.objects.all()


class RaffleRetrieveAPIView(RetrieveAPIView):
    serializer_class = RaffleSerializer
    queryset = RaffleExecution.objects.all()
