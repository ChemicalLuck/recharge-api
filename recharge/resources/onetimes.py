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
        return self.__base_post(self.url, ['write_subscriptions'], data)

    def retrieve(self, onetime_id):
        """Retrieve a onetime.\n
        Scopes: 'read_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/onetimes/onetimes_retrieve>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/onetimes/onetimes_retrieve>`_
        """
        return self.__base_get(f'{self.url}/{onetime_id}',
                               ['read_subscriptions'])

    def update(self, onetime_id, data):
        """Update a onetime.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/onetimes/onetimes_update>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/onetimes/onetimes_update>`_
        """
        return self.__base_put(f'{self.url}/{onetime_id}',
                               ['write_subscriptions'], data)

    def delete(self, onetime_id):
        """Delete a onetime.\n
        Scopes: 'write_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/onetimes/onetimes_delete>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/onetimes/onetimes_delete>`_
        """
        return self.__base_delete(f'{self.url}/{onetime_id}',
                                  ['write_subscriptions'])

    def list(self, data=None):
        """List onetimes.\n
        Scopes: 'read_subscriptions'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/onetimes/onetimes_list>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/onetimes/onetimes_list>`_
        """
        return self.__base_get(self.url, ['read_subscriptions'], data)
