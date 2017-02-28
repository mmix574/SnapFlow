from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$',views.IndexView.as_view()),
    url(r'^form/$',views.create),
    url(r'^post/$',views.PostView.as_view()),
    url(r'^post/create/',views.PostEditView.as_view()),
]