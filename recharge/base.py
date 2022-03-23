import logging

from recharge.constants import BASE_URL

import requests

from recharge.exceptions import InvalidScopeError

log = logging.getLogger(__name__)


class RechargeResource(object):
    base_url = BASE_URL
    object_key = None

    def __init__(self, api_key=None, version='2021-01', validate_scopes=False, debug=False, scopes=None):
        self.version = version
        self.debug = debug
        self.validate_scopes = validate_scopes
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

    def __base_request(self, method, url, required_scopes, data=None):
        if data is None:
            data = {}

        self.__check_scopes(required_scopes)

        request_to_call = getattr(requests, method)
        response = request_to_call(url, json=data, headers=self.headers)

        self.__log(url, response)

        if response.status_code == 429:
            return self.__base_request(method, url, data)
        return response.json()

    def __base_delete(self, url, required_scopes, data=None):
        return self.__base_request('delete', url, required_scopes, data)

    def __base_get(self, url, required_scopes, data=None):
        return self.__base_request('get', url, required_scopes, data)

    def __base_put(self, url, required_scopes, data=None):
        return self.__base_request('put', url, required_scopes, data)

    def __base_post(self, url, required_scopes, data=None):
        return self.__base_request('post', url, required_scopes, data)

    def __check_scopes(self, required_scopes: list[str]):
        if self.validate_scopes:
            if not all(scope in required_scopes for scope in self.scopes):
                raise InvalidScopeError(f"Method requires all scopes in: {required_scopes}.")
