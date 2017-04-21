from django.conf.urls import url


from . import views

from . import forum_api

urlpatterns = [
    url(r'(?P<id>[0-9]+)/$', views.DetailView.as_view(),name="_finding"),
    url(r'(?P<id>[0-9]+)/(?P<action>\w+)$', views.FindingActionView.as_view(), name="_finding_action"),

    url(r'^$',views.IndexView.as_view(),name="_finding"),
    url(r'^create/$',views.CreateView.as_view(),name="_asking"),
    url(r'^like/$', forum_api.add_like),
    url(r'^tag/', forum_api.get_tags),
]