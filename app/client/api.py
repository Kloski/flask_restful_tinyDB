import requests


class ApiClient(object):
    def __init__(self, backend_url):
        self.backend_url = backend_url

    def get_json_data(self, resource_path, jsonData):
        response = requests.get(self.backend_url + resource_path)

    def post_json_data(self, resource_path, jsonData):
        response = requests.post(
            self.backend_url + resource_path, data=jsonData)

    def put_json_data(self, resource_path, jsonData):
        response = requests.put(
            self.backend_url + resource_path, data=jsonData)
