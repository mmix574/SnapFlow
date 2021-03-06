"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include,url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


from forum.views import SearchView
urlpatterns = [
    # index
    url(r'^', include('index.urls')),
    # admin
    url(r'^admin/',admin.site.urls),
    # api
    url(r'^api/',include('api.urls')),
    # space
    url(r'^space/',include('space.urls')),
    # timeline
    url(r'^time/',include('timeline.urls')),
    # forum
    url(r'^t/',include('forum.urls')),
    #message
    url(r'^m/',include('message.urls')),
    #fake
    url(r'^fake/',include('fake.urls')),
    # history
    url(r'^history/',include('history.urls')),
    # collection
    url(r'^collection/',include('collection.urls')),
    # site_admin
    url(r'^a/',include('site_admin.urls')),
    # credit
    url(r'^credit/', include('credit.urls')),
    # group
    url(r'^g/', include('group.urls')),

                  #search
    url(r'^s$',SearchView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


