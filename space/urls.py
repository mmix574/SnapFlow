from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^userdata/$', views.UserDataView.as_view(),name="userdata"),
    url(r'^userprofile/$', views.UserProfileView.as_view(), name="user_profile"),
    url(r'^achieve/$',views.UserAchieveView.as_view(),name='user_achieve'),
]