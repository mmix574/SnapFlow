from django.conf.urls import url

from . import views
from . import v2views

urlpatterns = [
    # 欢迎界面，包括未登录欢迎界面和登陆之后的欢迎界面
    url(r'^$',views.IndexView.as_view(),name="_index"),
    # 提示消息
    # url(r'message',views.MessageView.as_view()),
    # 登陆
    url(r'^login/$',v2views.LoginView.as_view()),
    # 注册
    url(r'^register/$',v2views.RegisterView.as_view()),
    # 登出
    url(r'^logout$', views.LogoutView.as_view()),

    # 测试
    url(r'^username$',views.username),
    url(r'^test',views.TestView.as_view()),

    url(r'^passwordchange', views.PasswordChangeView.as_view()),
    url(r'^none$',views.NoneView.as_view()),

    # 2017年3月3日 20:07:22
    url(r'^w', v2views.V2Index.as_view()),
]