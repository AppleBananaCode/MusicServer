from django.conf.urls import include, url
from .views import getPlayListDetail
from .views import getTop_playlistsId
from .views import test3
from .views import test4
from .views import get_lyric

urlpatterns = [
    url(r'^hello/', getPlayListDetail),
    url(r'^hello1/', getTop_playlistsId),
    url(r'^hello2/', test3),
    url(r'^hello3/', test4),
    url(r'^hello4/', get_lyric)

]