from django.conf.urls import url

from . import views

from .json_api import get_everyday_sign_status
from .json_api import do_everyday_sign

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='credit'),
    url(r'^history/$', views.HistoryView.as_view(), name='credit_history'),
    url(r'^exchange/$', views.ExchangeView.as_view(), name='credit_exchange'),
    url(r'^achievement/', views.AchievementView.as_view(), name='credit_achievement'),
    url(r'signstatus/',get_everyday_sign_status),
    url(r'dosign/', do_everyday_sign),
]