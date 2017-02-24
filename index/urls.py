from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$',views.index),
<<<<<<< HEAD
    url(r'^login$',views.login)
=======
>>>>>>> f332e73866a28c53bec7ffb3263e1776783d1a05
]