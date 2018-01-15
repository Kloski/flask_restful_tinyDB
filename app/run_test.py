import requests
from app.server.api import db_client

PORT = 5000
SITE = 'http://127.0.0.1:{}/api/'.format(PORT)
REQUEST_URL = SITE + 'json'

''' Clear DB '''
db_client._clear_db()

''' New Object in DB '''
db_client.insert_json({'Object': '0', 'Value': 2048})

''' Get Whole DB and request for Object : 0 '''
print(db_client.get_all())
print(db_client.find_by_property_contains_value('Object', '0'))

''' Request PUT on Server '''
res = requests.put(REQUEST_URL + '/Object/0', json={'Value' : 0})
print(res)

''' Now Get New DB and request for Object : 0 '''
print(db_client.get_all())
print(db_client.find_by_property_contains_value('Object', '0'))
