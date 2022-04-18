from django.urls import path, re_path
from articles.views import article_archive

urlpatterns = [
    # 请求路径和视图函数的映射关系,一但请求路径和某一个path中的路径匹配成功，则调用改path中的视图函数
    re_path("(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})", article_archive),  # 关键字传参 $ 有相同匹配不会被覆盖

]
