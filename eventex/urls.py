from django.conf.urls import url, include
from django.contrib import admin
from eventex.core.views import home

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', home),
=======
    url(r'^$',home, name='home'),
    url(r'^inscricao/', include('eventex.subscriptions.urls',
                                namespace='subscriptions')),
>>>>>>> 1731772b53b6fe6f7060d384d410dd85f8a90e07
    url(r'^admin/', admin.site.urls),
]
