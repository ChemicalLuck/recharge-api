import logging

from recharge.constants import BASE_URL

import requests

log = logging.getLogger(__name__)


class BaseResource(object):
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

    @property
    def scopes(self):
        return self.scopes

    @staticmethod
    def response_handler(self, url, response):
        if response.status_code == 429:
            return self.base_delete(url)
        response.raise_for_status()
        return response.json()

    def base_delete(self, url):
        response = requests.delete(url, headers=self.headers)
        self.log(url, response)
        if response.status_code == 429:
            return self.base_delete(url)
        response.raise_for_status()
        return response.json()

    def base_get(self, url):
        response = requests.get(url, headers=self.headers)
        self.log(url, response)


