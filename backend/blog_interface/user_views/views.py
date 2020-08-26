import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def register_user(request):
    body = request.body
    return HttpResponse(f"注册mock!{body}")
