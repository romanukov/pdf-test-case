from flask import request
from flask.views import MethodView

from core.models import CustomerData
from core.service import Service


class CreateContractView(MethodView):
    service: Service
    
    def post(self):
        data = request.json
        try:
            customer_data = CustomerData(**data)
        except Exception:
            """
            Обрабатываем ошибки парсинга, возвращаем 400 ошибку
            """
            return ...
        
        return
