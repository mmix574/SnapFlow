from django.conf.urls import url

from .views import default_method
from .views import fake_user


urlpatterns = [
    url(r'$',default_method),
    url(r'user$', fake_user),
]
