from django.http import HttpResponse
from django.shortcuts import render
from api import NetEase
import simplejson
# Create your views here.

def test(request):
    ease = NetEase()
    s = ease.playlist_detail('105415765')


    return HttpResponse(s)


def test2(request):
    ease = NetEase()
    s = ease.top_playlists(limit=1)
    return HttpResponse(s)
