from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view()),
    url(r'^create/$',views.CreateView.as_view()),
    url(r'^new/$', views.NewView.as_view()),
]