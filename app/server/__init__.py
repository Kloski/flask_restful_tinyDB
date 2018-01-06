# -*- coding: utf-8 -*-
"""
Base server module.
"""

PORT = 5000


from flask import Flask, Blueprint
from flask_restful import Api
from app.server.api import JsonDataController, JsonParamsDataController, ObjectController, DummyController

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_blueprint)

api.add_resource(DummyController, '/dummy/<int:id>')
api.add_resource(JsonDataController, '/json')
api.add_resource(JsonParamsDataController, '/json/<int:id>')
api.add_resource(ObjectController, '/object')

flask_app = Flask(__name__)
flask_app.register_blueprint(api_blueprint)
