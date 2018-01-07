# -*- coding: utf-8 -*-
"""
REST API module.
"""

from flask_restful import reqparse, abort, Resource, marshal, fields
from flask import request

from app.server.db import TinyDBWrapper, db_client

parser = reqparse.RequestParser()


def marshall_object(item):
    obj_fields = {}
    for key in item.keys():
        obj_fields[key] = fields.String
    marshalled_item = marshal(item, obj_fields)


class JsonDataController(Resource):
    def get(self):
        """ Returns all JSON data """
        all = db_client.get_all()

        # result = []
        # for item in all:
        #     marshalled_item = marshall_object(item)
        #     result.append(marshalled_item)

        return all

    def post(self):
        json_data = request.json
        json_data2 = request.get_json(silent=True)
        # data = request.get_data()
        db_client.insert_json(json_data)

        return json_data, 201


class JsonParamsDataController(Resource):
    def get(self, prop, val):
        """ Returns all JSON data """
        return db_client.find_by_property_contains_value(prop, val)

    def put(self, prop, val):
        json_data = request.json
        db_client.update(prop, val, json_data)

        return json_data, 201


class DummyController(Resource):
    def get(self, id: int):
        result = {}

        for i in range(id):
            result[str(i)] = {'task': 'Say "Hello, World!"'}

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
