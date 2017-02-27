from django.conf.urls import url

from . import views
from . import apiviews

urlpatterns = [
    url(r'^$',views.default),
    url(r'^user_validate$',views.user_validate),
    url(r'^user_register', views.UserRegisterView.as_view()),
]