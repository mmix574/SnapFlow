from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
# Create your views here.

def user(request):
    return HttpResponse("api calling ...")


def default(request):
    return HttpResponse("default api calling ")

