from recharge.base import RechargeResource


class RechargeWebhook(RechargeResource):
    """
    `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/webhooks_endpoints>`_\n
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/webhooks_endpoints>`_
    """
    object_key = 'webhooks'

    def create(self, data):
        """Create a webhook\n
        Scopes: 'write_webhooks'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_create>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/webhooks_endpoints/webhooks_create>`_
        """
        return self.__base_post(self.url, ['write_webhooks'], data)

    def retrieve(self, webhook_id):
        """Retrieve a webhook.\n
        Scopes: 'read_webhooks'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_retrieve>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/webhooks_endpoints/webhooks_retrieve>`_
        """
        return self.__base_get(f'{self.url}/{webhook_id}', ['read_webhooks'])

    def update(self, webhook_id, data):
        """Update a webhook.\n
        Scopes: 'write_webhooks'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_update>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/webhooks_endpoints/webhooks_update>`_
        """
        return self.__base_put(f'{self.url}/{webhook_id}', ['write_webhooks'],
                               data)

    def delete(self, webhook_id):
        """Delete a webhook.\n
        Scopes: 'write_webhooks'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_delete>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/webhooks_endpoints/webhooks_delete>`_
        """
        return self.__base_delete(f'{self.url}/{webhook_id}',
                                  ['write_webhooks'])

    def list(self, data):
        """List webhooks.\n
        Scopes: 'read_webhooks'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_list>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/webhooks_endpoints/webhooks_list>`_
        """
        return self.__base_get(self.url, ['read_webhooks'], data)

    def test(self, webhook_id):
        """Test a webhook.\n
        Scopes: 'write_webhooks'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_test>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/webhooks_endpoints/webhooks_test>`_
        """
        return self.__base_post(f'{self.url}/{webhook_id}/test',
                                ['write_webhooks'], {})
