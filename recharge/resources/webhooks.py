from recharge.base import RechargeResource


class RechargeWebhook(RechargeResource):
    """

    """
    object_key = 'webhooks'

    def create(self, data):
        """Create a webhook
        https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_create
        """
        return self.__base_post(self.url, data)

    def retrieve(self, webhook_id):
        """Retrieve a webhook.
        https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_retrieve
        """
        return self.__base_get(f'{self.url}/{webhook_id}')

    def update(self, webhook_id, data):
        """Update a webhook.
        https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_update
        """
        return self.__base_put(f'{self.url}/{webhook_id}', data)

    def delete(self, webhook_id):
        """Delete a webhook.
        https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_delete
        """
        return self.__base_delete(f'{self.url}/{webhook_id}')

    def list(self, data):
        """List webhooks.
        https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_list
        """
        return self.__base_get(self.url, data)

    def test(self, webhook_id):
        """Test a webhook.
        https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_test
        """
        return self.__base_post(f'{self.url}/{webhook_id}/test', {})