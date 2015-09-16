from django.conf.urls import include, url
from .views import getPlayListDetail
from .views import getTop_playlistsId
from .views import test3

urlpatterns = [
    url(r'^hello/', getPlayListDetail),
    url(r'^hello1/', getTop_playlistsId),
    url(r'^hello2/', test3)

]