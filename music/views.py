#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from api import NetEase
import simplejson
# Create your views here.

getLists = []
# 获取top歌单的详细内容
def test(request):
    ease = NetEase()
    s = ease.playlist_detail('95537632')


    return HttpResponse(s)

# 获取top歌单Id
def getTop_playlistsId(request):
    getlistId = []
    getDict = {}
    #getDict.
    ease = NetEase()
    s = ease.top_playlists(limit=50)
    req = simplejson.dumps(s)
    getReq = simplejson.loads(req)
    print(getReq)
   # req = simplejson.loads(s)
    # 遍历整个字典取出需要的数据并加入到list
    for getid in getReq:
        global getLists
        getLists.append(getid["id"])

    return HttpResponse(getLists)


def test3(request):
    ease = NetEase()
    s = ease.song_detail('30590170')
    print(getLists)
    global getLists
    return HttpResponse(getLists)