from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AdminView.as_view(),name="__broadcasting"),
    url(r'^add-broadcast/$', views.AdminCreateBroadcastingView.as_view(), name="__add_broadcasting"),
    url(r'^send-broadcast/$', views.AdminSendBroadcastingView.as_view(), name="__send_broadcasting"),
    url(r'^broadcast-history/$', views.BroadCastHistoryView.as_view(), name="__broadcast_history"),

]