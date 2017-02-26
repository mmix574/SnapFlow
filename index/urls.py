from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view()),
    url(r'message',views.MessageView.as_view()),

    url(r'^login$',views.login),
    url(r'^register$',views.register),
    url(r'^about$',views.about),
    url(r'^username$',views.username),
    url(r'^logout$',views.logout),
    url(r'^test$',views.test)
]