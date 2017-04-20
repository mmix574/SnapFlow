from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='credit'),
    url(r'^history/$', views.HistoryView.as_view(), name='credit_history'),
    url(r'^exchange/$', views.ExchangeView.as_view(), name='credit_exchange'),
    url(r'^achievement/', views.AchievementView.as_view(), name='credit_achievement'),
]