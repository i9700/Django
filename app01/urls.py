from django.urls import path, re_path
from app01 import views

urlpatterns = [
    # 请求路径和视图函数的映射关系,一但请求路径和某一个path中的路径匹配成功，则调用改path中的视图函数
    path("timer/", views.get_timer),
    path("", views.index),
]
