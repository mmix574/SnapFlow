from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse




def default_method(request):
    return HttpResponse("fakeone")


class FakeUserView():
    pass