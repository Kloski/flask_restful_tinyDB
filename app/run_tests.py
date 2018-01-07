# -*- coding: utf-8 -*-
"""
Tests module.

Tests execution.
"""

from app.client import client
from app.server.api import db_client
from app.tests.server_api import send_random_json_data_to_backend, get_all_json_data, update_json_data


if __name__ == '__main__':
    db_client._clear_db()  # purge DB before tests
    send_random_json_data_to_backend(client)
    all = get_all_json_data(client)
    update_json_data(client)
