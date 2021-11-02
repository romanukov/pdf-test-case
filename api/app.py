"""
Запускает приложение с API
"""
from flask import Flask

from api.container import Container
from api.views import CreateContractView


# Разрешаем зависимости
Container().resolve_dependencies()

# Конфигурируем API
app = Flask(__name__)
app.add_url_rule('/create_contract/', view_func=CreateContractView.as_view('create_contract'))


