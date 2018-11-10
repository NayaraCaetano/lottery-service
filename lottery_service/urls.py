from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'raffle/', include('raffle.urls')),

    # Others
    url(r'^admin/', admin.site.urls),
]
