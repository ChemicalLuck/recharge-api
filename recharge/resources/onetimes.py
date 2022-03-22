from recharge.base import RechargeResource


class RechargeOnetime(RechargeResource):
    """
    `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/onetimes>`_\n
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/onetimes>`_
    """
    object_key = 'onetimes'

    def create(self, data):
        """Create a onetime.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/onetimes/onetimes_create>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/onetimes/onetimes_create>`_
        """
        self.__check_scopes(['write_subscriptions'])
        return self.__base_post(self.url, data)

    def retrieve(self, onetime_id):
        """Retrieve a onetime.\n
        Scopes: 'read_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/onetimes/onetimes_retrieve>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/onetimes/onetimes_retrieve>`_
        """
        self.__check_scopes(['read_subscriptions'])
        return self.__base_get(f'{self.url}/{onetime_id}')

    def update(self, onetime_id, data):
        """Update a onetime.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/onetimes/onetimes_update>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/onetimes/onetimes_update>`_
        """
        self.__check_scopes(['write_subscriptions'])
        return self.__base_put(f'{self.url}/{onetime_id}', data)

    def delete(self, onetime_id):
        """Delete a onetime.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/onetimes/onetimes_delete>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/onetimes/onetimes_delete>`_
        """
        self.__check_scopes(['write_subscriptions'])
        return self.__base_delete(f'{self.url}/{onetime_id}')

    def list(self, data=None):
        """List onetimes.\n
        Scopes: 'read_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/onetimes/onetimes_list>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/onetimes/onetimes_list>`_
        """
        self.__check_scopes(['read_subscriptions'])
        return self.__base_get(self.url, data)