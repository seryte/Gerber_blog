from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def joint_debugging(request):
    return HttpResponse("注册mock!")