from django.shortcuts import render, HttpResponse
from datetime import datetime


# Create your views here.
def get_timer(request):
    '''

    :param request:
    :return:HttpResponse对象
    '''
    # 获取数据
    # return HttpResponse("Hello Django!")
    now_time = datetime.now().strftime("%Y-%m-%d %X")
    return render(request, "app01/timer.html", {"now": now_time})


def index(request):
    # 返回客户端一个简单字符串
    # return HttpResponse("index...")
    return render(request, "app01/index.html")


def show(request, mobile):
    print("mobile:", mobile, type(mobile))
    return HttpResponse(f"hi,{mobile}用户！")
