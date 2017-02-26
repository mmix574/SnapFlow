from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.default),
    url(r'^member/$', views.MemberView.as_view())
]