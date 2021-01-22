import requests
import common.logging_requests as request

class Config:
    def __init__(self, config):
        self.config = config
        self.auth=self._get_auth()

    def _get_auth(self):
        if 'PASSWORD' in self.config:
            return self._get_password_auth()
        elif 'KEY' in self.config:
            return self._get_key_auth()

    def _get_password_auth(self):
        return True

    def _get_key_auth(self):
        return True


class Client:
    def __init__(self, config):
        self.config = Client(config) if isinstance(config, dict) else config

    def post(self, endpoint, **kwargs):
        return self.send("POST", endpoint, **kwargs)

    def send(self, method, endpoint, **kwargs):
        url = self._construct_url(endpoint)
        response = request.send(method, url, **kwargs)

        return response

    def _construct_url(self, endpoint):
        base_url = self.config['BASE_URL']
        endpoint = endpoint.lstrip("/")
        return "{}/{}".format(base_url, endpoint)




headers = {
    'x-rapidapi-key': "509f38e375msh6abbb017c4c26e9p199762jsnfd9789ef92e0",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
}
