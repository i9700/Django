from django.shortcuts import render, HttpResponse


# Create your views here.

def article_detail(request):
    return HttpResponse("2012/12 文章")


def article_archive(request, year, month):
    # 查询年月的文章
    # print(year)
    # print(month[0:2], type(month))
    return HttpResponse("{}年{}月 文章".format(year, month))
