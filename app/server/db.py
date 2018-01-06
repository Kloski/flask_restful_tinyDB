# -*- coding: utf-8 -*-
"""
Module with DB queries.

Useful links: 
http://pythonmonthly.com/tinydb-intro.html
"""

from tinydb import TinyDB, Query


class TinyDBWrapper(object):
    def __init__(self, db: TinyDB):
        self.db = db
        self.query = Query()

    def _get_query_property(self, property_name):
        return getattr(self.query, property_name)

    def _get_search_query(self, property_name, property_value):
        return self._get_query_property(property_name).search(property_value)

    def get_all(self):
        return self.db.all()

    def insert_json(self, json_data):
        self.db.insert(json_data)

    def find_by_property_has_value(self, property_name, property_value):
        self.db.search(self._get_query_property(
            property_name) == property_value)

    def find_by_property_contains_value(self, property_name, property_value):
        self.db.search(self._get_search_query(property_name, property_value))

    def update(self, property_name, property_value, updated_data):
        self.db.update(updated_data, self._get_search_query(
            property_name, property_value))

    def remove_by_criteria(self, property_name, property_value):
        self.db.remove(self._get_search_query(property_name, property_value))


db = TinyDB('fileTinyDB.json')
db_client = TinyDBWrapper(db)
