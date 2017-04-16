from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AdminView.as_view(),name="__broadcasting"),
    url(r'^abc/$', views.AdminCreateBroadcastingView.as_view(), name="__add_broadcasting"),
    url(r'^sbc/$', views.AdminSendBroadcastingView.as_view(), name="__send_broadcasting"),
]