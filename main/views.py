from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("こんにちは")

def hobby(request):
    return HttpResponse("私の趣味は吹奏楽です。")

def greet(request, name):
    message = "こんにちは" + name + "さん"
    return HttpResponse(message)