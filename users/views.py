from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse


# Create your views here.

def index(request):
    # 获取请求方式
    print(request.method)  # GET

    # 发送POST请求时获取数据的方式
    # print(request.body)
    # print(request.POST)  # 只有数据格式是urlencoded
    # users = request.POST.get("users")
    # pwd = request.POST.get("pwd")
    # hobby = request.POST.getlist("hobby")
    # print(users, pwd, hobby)

    # 发送GET请求获取数据
    # print(request.GET)

    # 获取请求路径
    # print(request.path)
    # print(request.get_full_path())  # 完整路径带参数

    # 获取请求头数据
    # print(request.META)
    # print(request.META.get("HTTP_HOST"))
    # return HttpResponse("ok")
    # return HttpResponse("您访问的资源不存在", status=404)  # 返回的HTTP响应状态码
    # return HttpResponse("<h1>ok</h1>", content_type="text/plain")  # 返回数据类型
    # 自定义响应头
    # res = HttpResponse("ok")
    # res["users"] = "tao"
    # return res
    # return HttpResponse("ok")

    # 响应json数据
    # book = {"title": "生物密码", "price": 199}
    # import json
    # return HttpResponse(json.dumps(book, ensure_ascii=False), content_type="application/json")
    # 序列化一个字典数据
    # return JsonResponse(book)

    # 序列化一个列表数据
    # books = [{"title": "生物密码", "price": 199}, {"title": "三国演义", "price": 199}]
    # return JsonResponse(books, safe =False)
    print(request.META)
    ip = request.META.get("REMOTE_ADDR")
    return render(request, "users/index.html", {"ip": ip})


def login(request):
    return render(request, "users/login.html")


def auth(request):
    # 获取数据
    print("request.POST", request.POST)
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")

    # 模拟数据校验
    if user == "admin" and pwd == "123":

        # return HttpResponse("验证通过")
        return redirect("/users/")
    else:
        # return HttpResponse("用户名或者密码错误")
        return redirect("/users/login")
