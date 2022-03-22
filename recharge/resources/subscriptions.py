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
        self.__check_scopes(['write_subscriptions'])
        return self.__base_post(self.url, data)

    def retrieve(self, subscription_id):
        """Retrieve a subscription.\n
        Scopes: 'read_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_retrieve>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_retrieve>`_
        """
        self.__check_scopes(['read_subscriptions'])
        return self.__base_get(f'{self.url}/{subscription_id}')

    def update(self, subscription_id, data):
        """Update a subscription.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_update>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_update>`_
        """
        self.__check_scopes(['write_subscriptions'])
        return self.__base_put(f'{self.url}/{subscription_id}', data)

    def delete(self, subscription_id):
        """Delete a subscription.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_delete>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_delete>`_
        """
        self.__check_scopes(['write_subscriptions'])
        return self.__base_delete(f'{self.url}/{subscription_id}')

    def list(self, data=None):
        """List subscriptions.\n
        Scopes: 'read_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_list>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_list>`_
        """
        self.__check_scopes(['read_subscriptions'])
        return self.__base_get(self.url, data)

    @recharge_v1
    def count(self, data=None):
        """Count subscriptions.\n
        Scopes: 'read_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_count>`_
        """
        self.__check_scopes(['read_subscriptions'])
        return self.__base_get(f'{self.url}/count', data)

    def change_next_charge_date(self, subscription_id, date):
        """Change the next charge date of a subscription.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_change_next_charge>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_change_next_charge>`_
        """
        self.__check_scopes(['write_subscriptions'])
        return self.__base_post(
            f'{self.url}/{subscription_id}/set_next_charge_date',
            {'date': date}
        )

    def change_address(self, subscription_id, address_id):
        """Change a subscription address.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_change_address>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_change_address>`_
        """
        self.__check_scopes(['write_subscriptions'])
        return self.__base_post(
            f'{self.url}/{subscription_id}/change_address',
            {"address_id": address_id}
        )

    def cancel(self, subscription_id, data=None):
        """Cancel a subscription.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_cancel>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_cancel>`_
        """
        self.__check_scopes(['write_subscriptions'])
        return self.__base_post(f'{self.url}/{subscription_id}/cancel', data)

    def activate(self, subscription_id):
        """Activate a cancelled subscription.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_activate>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_activate>`_
        """
        self.__check_scopes(['write_subscriptions'])
        return self.__base_post(f'{self.url}/{subscription_id}/activate', {})

    @recharge_v1
    def create_bulk(self, address_id, data):
        """Bulk create subscriptions for address.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_create>`_
        """
        self.__check_scopes(['write_subscriptions'])
        return self.__base_post(
            f'{self.base_url}/addresses/{address_id}/subscriptions-bulk',
            data
        )

    @recharge_v1
    def update_bulk(self, address_id, data):
        """Bulk update subscriptions for address.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_update>`_
        """
        self.__check_scopes(['write_subscriptions'])
        return self.__base_put(
            f'{self.base_url}/addresses/{address_id}/subscriptions-bulk',
            data
        )

    @recharge_v1
    def delete_bulk(self, address_id, data):
        """Bulk delete subscriptions for address.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_delete>`_
        """
        self.__check_scopes(['write_subscriptions'])
        return self.__base_delete(
            f'{self.base_url}/addresses/{address_id}/subscriptions-bulk',
            data
        )
