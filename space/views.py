from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

def default(request):
    return HttpResponseRedirect('/space/member/')

def member(request):
    return HttpResponse("hello member...")
