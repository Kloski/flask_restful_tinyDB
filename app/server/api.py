# -*- coding: utf-8 -*-
"""
REST API module.
"""

from flask_restful import reqparse, abort, Resource
from flask import request

from app.server.db import TinyDBWrapper, db_client
from app.common.model import *

parser = reqparse.RequestParser()


class JsonDataController(Resource):
    def get(self):
        """ Returns all JSON data """
        return db_client.get_all()

    def post(self):
        _json_data = parser.parse_args()
        json_data = request.json
        db_client.insert_json(json_data)

        return json_data, 201


class JsonParamsDataController(Resource):
    def get(self, prop, val):
        """ Returns all JSON data """
        return db_client.find_by_property_contains_value(prop, val)

    def put(self, prop, val):
        json_data = parser.parse_args(strict=False)
        db_client.update(prop, val, json_data)

        return json_data, 201


class DummyController(Resource):
    def get(self, id: int):
        result = {}

        for i in range(id):
            result.i = {'task': 'Say "Hello, World!"'}

        return result

    def delete(self, id: int):
        abort(404, message="Dummy {} you can not DELETE!".format(id))
        return {'id': id}, 204

    def put(self, id: int):
        abort(404, message="Dummy {} you can not PUT!".format(id))
        return {'id': id}, 201

    def post(self, id: int):
        abort(404, message="Dummy {} you can not POST!".format(id))
        return {'id': id}, 201


class ObjectController(Resource):
    pass
