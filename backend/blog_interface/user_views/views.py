import json
import logging

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from blog_interface.Exception.my_exception import MyException
from blog_interface.Form.user import UserForm
from blog_interface.common import common

log = logging.getLogger('user.view')


class UserViews(View):
    def post(self, request, *args, **kwargs):
        body = request.body
        params = json.loads(body)
        form = UserForm(params)
        result = form.is_valid()

        if result:
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'],
                                            email=form.cleaned_data['email'])

            if user:
                login(request, user)
                return common.response_success()
            else:
                raise MyException("注册失败")
        else:
            log.error(form.errors.as_json())
            raise MyException()
