from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name="_finding"),
    url(r'^create/$',views.CreateView.as_view(),name="_asking"),
]