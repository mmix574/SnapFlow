from django.conf.urls import url

from .views import default_method

urlpatterns = [
    url(r'^$',default_method),
]