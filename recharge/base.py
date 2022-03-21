import logging

from recharge.constants import BASE_URL

import requests

log = logging.getLogger(__name__)


class RechargeResource(object):
    base_url = BASE_URL
    object_key = None

    def __init__(self, api_key=None, version='2021-01', debug=False, scopes=None):
        self.version = version
        self.debug = debug
        self.scopes = scopes
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Recharge-Access-Token': api_key,
            'X-Recharge-Version': version
        }

    def log(self, url, response):
        if self.debug:
            log.info(url)
            log.ingo(response.headers['X-Recharge-Limit'])

    @property
    def url(self):
        return f'{self.base_url}/{self.object_key}'

    def __base_request(self, method, url, data=None):
        method_to_call = getattr(requests, method)
        response = method_to_call(url, json=data, headers=self.headers)
        self.log(url, response)
        if response.status_code == 429:
            return self.__base_request(method, url, data)
        return response.json()

    def __base_delete(self, url):
        return self.__base_request('delete', url)

    def __base_get(self, url, data):
        return self.__base_request('get', url, data)

    def __base_put(self, url, data):
        return self.__base_request('put', url, data)

    def __base_post(self, url, data):
        return self.__base_request('post', url, data)