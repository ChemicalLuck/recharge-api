import logging
import time
from typing import Any, Mapping

import requests

from recharge.api.tokens import TokenScope

log = logging.getLogger(__name__)


class RechargeResource(object):
    """
    Resource from the Recharge API. This class handles
    logging, sending requests, parsing JSON, and rate
    limiting.

    Refer to the API docs to see the expected responses.
    https://developer.rechargepayments.com/
    """

    base_url = "https://api.rechargeapps.com"
    object_list_key = None

    def __init__(
        self, access_token=None, debug=False, scopes: list[TokenScope] | None = None
    ):
        self.debug = debug
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Recharge-Access-Token": access_token,
        }
        self.scopes = scopes
        self.allowed_endpoints = []

    def check_scopes(self, endpoint: str, scopes: list[TokenScope]):
        if endpoint in self.allowed_endpoints:
            return

        if not self.scopes:
            raise ValueError("No scopes found for token.")

        missing_scopes = []

        for scope in scopes:
            if scope not in self.scopes:
                missing_scopes.append(scope)

        if missing_scopes:
            raise ValueError(f"Endpoint {endpoint} missing scopes: {missing_scopes}")
        else:
            self.allowed_endpoints.append(endpoint)

    def log(self, url, response):
        if self.debug:
            log.info(url)
            log.info(response.headers["X-Recharge-Limit"])

    @property
    def url(self) -> str:
        return f"{self.base_url}/{self.object_list_key}"

    def http_delete(self, url: str, body: Mapping[str, Any] | None = None):
        response = requests.delete(url, headers=self.headers, json=body)
        log.info(url)
        log.info(response.headers["X-Recharge-Limit"])
        if response.status_code == 429:
            return self.http_delete(url)
        return response

    def http_get(self, url: str, query: Mapping[str, Any] | None = None):
        response = requests.get(url, params=query, headers=self.headers)
        self.log(url, response)
        if response.status_code == 429:
            time.sleep(1)
            return self.http_get(url)
        return response.json()

    def http_put(
        self,
        url: str,
        body: Mapping[str, Any] | None = None,
        query: Mapping[str, Any] | None = None,
    ):
        response = requests.put(url, json=body, params=query, headers=self.headers)
        self.log(url, response)
        if response.status_code == 429:
            time.sleep(1)
            return self.http_put(url, body)
        return response.json()

    def http_post(
        self,
        url: str,
        body: Mapping[str, Any] | None = None,
        query: Mapping[str, Any] | None = None,
    ):
        response = requests.post(url, json=body, params=query, headers=self.headers)
        self.log(url, response)
        if response.status_code == 429:
            time.sleep(1)
            return self.http_post(url, body)
        return response.json()
