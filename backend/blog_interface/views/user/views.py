import json
import logging

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# Create your views here.
from django.views import View

from blog_interface.Exception.my_exception import MyException
from blog_interface.Form.user import UserForm
from blog_interface.common.common import response_failed, response_success

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
                return response_success()
            else:
                raise MyException("注册失败")
        else:
            log.error(form.errors.as_json())
            raise MyException()


class UserLogin(View):
    def post(self, request, *args, **kwargs):
        body = request.body
        data = json.loads(body, encoding="utf-8")
        user_form = UserForm(data)
        if not user_form.is_valid():
            return response_failed("登录失败，用户名或密码错误")

        user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
        if not user:
            return response_failed(message="登录失败")
        else:
            login(request, user)
            return response_success(message="登录成功")
