from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    # 获取请求方式
    print(request.method)  # GET

    # 发送POST请求时获取数据的方式
    # print(request.body)
    # print(request.POST)  # 只有数据格式是urlencoded
    # user = request.POST.get("user")
    # pwd = request.POST.get("pwd")
    # hobby = request.POST.getlist("hobby")
    # print(user, pwd, hobby)

    # 发送GET请求获取数据
    print(request.GET)

    # 获取请求路径
    print(request.path)
    print(request.get_full_path())  # 完整路径带参数

    # 获取请求头数据
    print(request.META)
    print(request.META.get("HTTP_HOST"))
    return HttpResponse("ok")
