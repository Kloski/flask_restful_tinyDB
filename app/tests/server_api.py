import requests
from app.client.api import ApiClient


def send_random_json_data_to_backend(client: ApiClient):
    response = requests.get("http://api.open-notify.org/astros.json")
    randomServerData = response.json()

    for item in randomServerData['people']:
        response = client.post_json_data('json', item)
        print(response)


def get_all_json_data(client: ApiClient):
    all_data = client.get_json_data('json')
    return all_data


def update_json_data(client: ApiClient):
    dummy = client.get_json_data('dummy/2')
    all = get_all_json_data(client)

    response = client.put_json_data(f'json/craft/ISS', {"name": "Fero Taraba"})

    for item in all:
        for key in item.keys():
            val = item[key]
            response = client.put_json_data(f'json/{key}/{val}', dummy)

    all_dummy = get_all_json_data(client)
    test_pass = all_dummy == all
