from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CollectionView.as_view(),name="_collection"),
    url(r'^add$', views.add_collection, name="add_collection"),
]