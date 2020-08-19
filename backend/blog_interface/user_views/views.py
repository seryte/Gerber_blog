import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def register_user(request):
    body = request.body
    data = json.loads(body, encoding='utf-8')
    print(data)
    # user_name = request.get("username", "")
    # user_email = request.get()
    return HttpResponse(f"注册mock!{data}")
