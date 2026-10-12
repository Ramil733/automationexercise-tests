import requests


class BaseApi:
    BASE_URL = "https://automationexercise.com/api"

    def __init__(self):
        self.session = requests.Session()

    def get(self, endpoint: str, **kwargs):
        return self.session.get(f"{self.BASE_URL}{endpoint}", **kwargs)

    def post(self, endpoint: str, data=None, **kwargs):
        return self.session.post(f"{self.BASE_URL}{endpoint}", data=data, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self.session.delete(f"{self.BASE_URL}{endpoint}", **kwargs)