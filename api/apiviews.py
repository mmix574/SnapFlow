from django.http.response import JsonResponse
from django.http.response import HttpResponse

from django.views.generic.base import View

class ApiView(View):

    def get(self, header, alternate=None):
        return HttpResponse("hello world")
