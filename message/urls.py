from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='_messaging'),
    url(r'^sm$',views.SystemMessageView.as_view(),name='system_message'),
]