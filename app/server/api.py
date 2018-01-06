# -*- coding: utf-8 -*-
"""
REST API module.
"""

from flask import Blueprint
from flask_restful import Api, Resource, url_for

from app.common.model import *


api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_blueprint)


class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}


api.add_resource(TodoItem, '/todos/<int:id>')
