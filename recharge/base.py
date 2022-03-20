import logging

from recharge.constants import BASE_URL

import requests

log = logging.getLogger(__name__)


class RechargeResource(object):
    base_url = BASE_URL
    object_key = None

    def __init__(self, api_key=None, debug=False, scopes=None):
        self.debug = debug
        self.scopes = scopes
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Recharge-Access-Token': api_key
        }

    def log(self, url, response):
        if self.debug:
            log.info(url)
            log.ingo(response.headers['X-Recharge-Limit'])

    @property
    def url(self):
        return f'{self.base_url}/{self.object_key}'

    def _base_request(self, method, url, data=None):
        method_to_call = getattr(requests, method)
        response = method_to_call(url, json=data, headers=self.headers)
        self.log(url, response)
        if response.status_code == 429:
            return self._base_request(method, url, data)
        return response.json()

    def base_delete(self, url):
        return self._base_request('delete', url)

    def base_get(self, url, data):
        return self._base_request('get', url, data)

    def base_put(self, url, data):
        return self._base_request('put', url, data)

    def base_post(self, url, data):
        return self._base_request('post', url, data)

    def create(self, data):
        return self.base_post(self.url, data)

    def update(self, resource_id, data):
        return self.base_put(f'{self.url}/{resource_id}', data)

    def retrieve(self, resource_id):
        return self.base_get(f'{self.url}/{resource_id}')

    def list(self, data):
        return self.base_get(self.url, data)