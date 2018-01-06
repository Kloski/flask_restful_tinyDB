# -*- coding: utf-8 -*-
"""
Base server module.
"""

from flask import Flask
from app.server.api import api_blueprint

flask_app = Flask(__name__)
flask_app.register_blueprint(api_blueprint)


from tinydb import TinyDB, Query

db = TinyDB('fileTinyDB.json')
