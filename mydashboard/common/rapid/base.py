import requests


class RapidApi:
    def __init__(self, username=None, password=None, url=None, headers=None, params=None):
        self.username = username
        self.password = password
        self.url = url
        self.headers = headers
        self.params = params

    def get(self):
        response = requests.get(self.url, self.headers, params=self.params)

        if response.status_code != 200:
            raise ValueError('Status Code received from rapid is {}'.format(response.status_code))

        return response.json()
