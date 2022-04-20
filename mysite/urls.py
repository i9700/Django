"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include, register_converter
from articles.views import article_detail
from articles.views import article_archive
from app01.views import show


class MobileConverter():
    # 正则规则
    regex = "1[3-9]\d{9}"

    def to_python(self, value):
        return int(value)


register_converter(MobileConverter, "mobile")  # "mobile" ：别名
urlpatterns = [
    # 请求路径和视图函数的映射关系,一但请求路径和某一个path中的路径匹配成功，则调用改path中的视图函数
    path('admin/', admin.site.urls),
    # path("timer/", views.get_timer),
    # path("", views.index),
    # path("articles/2012/12/", article_detail),
    # 正则简单分组
    # re_path("articles/(\d{4})/(\d{1,2})", article_archive),  # 正则路由,位置传参
    # 有名分组
    # re_path("articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})", article_archive),  # 关键字传参 $ 有相同匹配不会被覆盖

    # 路由分发
    path("home/", include("app01.urls")),
    path("articles", include("articles.urls")),

    # 路由转发
    path("index/<mobile:mobile>", show),  # 左边mobile：规则 ，右边mobile：传入的关键字参数

    path("users/", include("users.urls"))
]
