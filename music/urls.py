from django.conf.urls import include, url
from .views import test
from .views import getTop_playlistsId
from .views import test3

urlpatterns = [
    url(r'^hello/', test),
    url(r'^hello1/', getTop_playlistsId),
    url(r'^hello2/', test3)

]