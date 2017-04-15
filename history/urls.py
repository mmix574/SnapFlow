from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HistoryView.as_view(),name="_history"),
]