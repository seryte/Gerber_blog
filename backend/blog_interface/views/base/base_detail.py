import json

from django.forms import model_to_dict
from django.views.generic import View

from interface_app.forms.service_form import ServiceForm
from interface_app.libs.respone import response_success, response_failed, ErrorCode
from interface_app.models.service import Service


class MyBaseDetailView(View):
    model = Service
    form = ServiceForm
    code = ErrorCode.common

    def get(self, request, base_id, *args, **kwargs):
        service = self.model.objects.filter(id=base_id).first()
        if not service:
            return response_failed(code=self.code, message="数据不存在！")
        return response_success(model_to_dict(service))

    def put(self, request, base_id, *args, **kwargs):
        body = request.body
        data = json.loads(body, encoding="utf-8")

        form = self.form(data)
        if not form.is_valid():
            return response_failed()

        service = self.model.objects.filter(id=base_id).first()
        if not service:
            return response_failed(code=ErrorCode.common, message="数据不存在！")

        self.model.objects.filter(id=base_id).update(**form.cleaned_data)  # 这里返回是id
        service = self.model.objects.filter(id=base_id).first()
        return response_success(model_to_dict(service))

    def patch(self, request, base_id, *args, **kwargs):
        self.put(request, base_id, *args, **kwargs)

    def delete(self, request, base_id, *args, **kwargs):
        self.model.objects.filter(id=base_id).delete()
        return response_success()
