from django.conf.urls import url

from raffle.views import RaffleListCreateAPIView, RaffleRetrieveAPIView

urlpatterns = [
    url(r'^$', RaffleListCreateAPIView.as_view(), name='raffles'),
    url(r'^(?P<pk>[0-9]+)', RaffleRetrieveAPIView.as_view(), name='raffle_details'),
]
