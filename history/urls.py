from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HistoryView.as_view(),name="_history"),
    url(r'^asking/$', views.HistoryAskingView.as_view(), name="_history_asking"),
    url(r'^answering/$', views.HistoryAnsweringView.as_view(), name="_history_answering"),
    url(r'^liking/$', views.HistoryLikingView.as_view(), name="_history_liking"),
    url(r'^collecting/$', views.HistoryLikingView.as_view(), name="_history_collecting"),

]