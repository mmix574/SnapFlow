from django.conf.urls import url

from . import views


from . import message_api
urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='_messaging'),
    url(r'^system-message/$',views.SystemMessageView.as_view(),name='system_message'),
    url(r'^private-message/$', views.PrivateMessageView.as_view(), name='private_message'),
    url(r'^message-status/$', views.MessageStatusView.as_view(), name='message_status'),
    url(r'^event-message/$', views.EventMessageView.as_view(), name='event_message'),
    url(r'^friend/$', views.FriendView.as_view(), name='space-friend'),
    url(r'sessionclose/',message_api.close_session),
]