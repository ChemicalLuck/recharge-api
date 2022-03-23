from recharge.base import RechargeResource
from recharge.decorators import recharge_v1


class RechargeSubscription(RechargeResource):
    """
    `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions>`_\n
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions>`_
    """
    object_key = 'subscriptions'

    def create(self, data):
        """Create a subscription.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_create>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_create>`_
        """
        return self.__base_post(self.url, ['write_subscriptions'], data)

    def retrieve(self, subscription_id):
        """Retrieve a subscription.\n
        Scopes: 'read_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_retrieve>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_retrieve>`_
        """
        return self.__base_get(f'{self.url}/{subscription_id}',
                               ['read_subscriptions'])

    def update(self, subscription_id, data):
        """Update a subscription.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_update>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_update>`_
        """
        return self.__base_put(f'{self.url}/{subscription_id}',
                               ['write_subscriptions'], data)

    def delete(self, subscription_id):
        """Delete a subscription.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_delete>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_delete>`_
        """
        return self.__base_delete(f'{self.url}/{subscription_id}',
                                  ['write_subscriptions'])

    def list(self, data=None):
        """List subscriptions.\n
        Scopes: 'read_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_list>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_list>`_
        """
        return self.__base_get(self.url, ['read_subscriptions'], data)

    @recharge_v1
    def count(self, data=None):
        """Count subscriptions.\n
        Scopes: 'read_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_count>`_
        """
        return self.__base_get(f'{self.url}/count', ['read_subscriptions'],
                               data)

    def change_next_charge_date(self, subscription_id, date):
        """Change the next charge date of a subscription.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_change_next_charge>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_change_next_charge>`_
        """
        return self.__base_post(
                f'{self.url}/{subscription_id}/set_next_charge_date',
                ['write_subscriptions'], {'date': date})

    def change_address(self, subscription_id, address_id):
        """Change a subscription address.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_change_address>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_change_address>`_
        """
        return self.__base_post(f'{self.url}/{subscription_id}/change_address',
                                ['write_subscriptions'],
                                {"address_id": address_id})

    def cancel(self, subscription_id, data=None):
        """Cancel a subscription.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_cancel>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_cancel>`_
        """
        return self.__base_post(f'{self.url}/{subscription_id}/cancel',
                                ['write_subscriptions'], data)

    def activate(self, subscription_id):
        """Activate a cancelled subscription.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_activate>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_activate>`_
        """
        return self.__base_post(f'{self.url}/{subscription_id}/activate',
                                ['write_subscriptions'], {})

    @recharge_v1
    def create_bulk(self, address_id, data):
        """Bulk create subscriptions for address.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_create>`_
        """
        return self.__base_post(
                f'{self.base_url}/addresses/{address_id}/subscriptions-bulk',
                ['write_subscriptions'], data)

    @recharge_v1
    def update_bulk(self, address_id, data):
        """Bulk update subscriptions for address.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_update>`_
        """
        return self.__base_put(
                f'{self.base_url}/addresses/{address_id}/subscriptions-bulk',
                ['write_subscriptions'], data)

    @recharge_v1
    def delete_bulk(self, address_id, data):
        """Bulk delete subscriptions for address.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_delete>`_
        """
        return self.__base_delete(
                f'{self.base_url}/addresses/{address_id}/subscriptions-bulk',
                ['write_subscriptions'], data)
