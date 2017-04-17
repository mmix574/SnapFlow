from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='_messaging'),
    url(r'^system-message$',views.SystemMessageView.as_view(),name='system_message'),
    url(r'^private-message$', views.PrivateMessageView.as_view(), name='private_message'),
    url(r'^message-status$', views.MessageStatusView.as_view(), name='message_status'),
]