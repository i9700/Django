from django.shortcuts import render, HttpResponse

# Create your views here.
def get_timer(request):
    '''

    :param request:
    :return:HttpResponse对象
    '''
    return HttpResponse("Hello Django!")


def index(request):
    return HttpResponse("index...")
