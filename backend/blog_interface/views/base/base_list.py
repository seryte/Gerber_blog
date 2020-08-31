import json

from django.forms import model_to_dict
from django.http import HttpResponse
from django.views.generic import View

from interface_app.forms.service_form import ServiceForm
from interface_app.libs.respone import response_success, response_failed, ErrorCode
from interface_app.models.service import Service
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class MyBaseListView(View):
    model = Service
    form = ServiceForm
    code = ErrorCode.common

    def get(self, request, *args, **kwargs):
        """
        获取列表
        :param args:
        :param kwargs:
        :return:
        """
        services = self.model.objects.all()
        page = request.GET.get('page')
        page_size = request.GET.get('pageSize')
        paginator = Paginator(services, page_size)
        count = len(services)

        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # 如果页数不是整型, 取第一页.
            contacts = paginator.page(1)
        except EmptyPage:
            # 如果页数超出查询范围，取最后一页
            contacts = paginator.page(paginator.num_pages)

        ret = []
        for s in contacts:
            t = model_to_dict(s)
            ret.append(t)
        return response_success(ret, page=page, pagesize=page_size, count=count)

    def post(self, request, *args, **kwargs):
        """
        新增数据
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        data = json.loads(body, encoding="utf-8")

        form = self.form(data)
        if not form.is_valid():
            return response_failed(code=self.code)

        service = self.model.objects.create(**form.cleaned_data)

        if not service:
            return response_failed(code=ErrorCode.service)
        else:
            return response_success(model_to_dict(service))
