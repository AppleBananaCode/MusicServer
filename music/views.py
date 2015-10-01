#!/usr/bin/env python
# -*- coding: utf-8 -*-
from this import s

from django.http import HttpResponse
from django.shortcuts import render
from api import NetEase
import simplejson
# Create your views here.

getLists = []
getListImage = []
getListName = []

getSongIDs = []
# 获取top歌单的详细内容
def getPlayListDetail(request):
    sendJsonAll = []
    global getSongIDs
    getSongIDs = []
    getSongTimes = []
    getSongNames = []
    getSongMp3Url = []
    getId = simplejson.loads(request.body)
    print(getId)
    id = getId["id"]
    ease = NetEase()
    s = ease.playlist_detail(id)
    jsonData = simplejson.dumps(s)
    parjson = simplejson.loads(jsonData)

    print(parjson)

    for getKeys in parjson:
        global getSongIDs
        getSongIDs.append(getKeys["id"])

        getSongNames.append(getKeys["name"])
        getSongTimes.append(getKeys["duration"])
        getSongMp3Url.append(getKeys["mp3Url"])

    sendJsonAll.append(getSongIDs)
    sendJsonAll.append(getSongNames)
    sendJsonAll.append(getSongTimes)
    sendJsonAll.append(getSongMp3Url)
    global getSongIDs
    sendJsonData = simplejson.dumps(sendJsonAll)
    print(sendJsonData)
    return HttpResponse(sendJsonData)

# 获取top歌单Id
def getTop_playlistsId(request):
    getlistAll = []
    global getLists
    getLists = []
    global getListName
    getListName = []
    global getListImage
    getListImage = []

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
        global getListName
        getListName.append(getid["name"])
        global getListImage
        getListImage.append(getid["coverImgUrl"])

    getlistAll.append(getLists)
    getlistAll.append(getListName)
    getlistAll.append(getListImage)

    jsonArray = simplejson.dumps(getlistAll)


    return HttpResponse(jsonArray)


def test3(request):
    ease = NetEase()
    s = ease.song_detail('22754251')
    p = simplejson.dumps(s)
    global getLists
    return HttpResponse(p)


def test4(request):
    ease = NetEase()
    s = ease.playlist_detail("104596111")
    jsonData = simplejson.dumps(s)
    return HttpResponse(jsonData)

def get_lyric(request):

    lyricId = simplejson.loads(request.body)
    print(lyricId)

    ids = lyricId['id']
    print(ids)
    s = NetEase()
    getly = s.song_lyric(ids)
    print(getly)
    sendDict = dict()
    sendDict["id"] = getly
    sendly = simplejson.dumps(sendDict)

    return HttpResponse(sendly)

# 获得热门歌手
def getTopSinger(request):
    ease = NetEase()
    s = ease.top_artists(0,10)
    jsonData = simplejson.dumps(s)
    return HttpResponse(jsonData)