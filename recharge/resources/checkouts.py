from recharge.base import RechargeResource


class RechargeCheckout(RechargeResource):
    """
    `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/checkouts>`_\n
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/checkouts>`_
    """
    object_key = 'checkouts'

    def create(self, data):
        """Create a checkout.\n
        Scopes: 'write_checkouts'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/checkouts/checkout_create>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/checkouts/checkout_create>`_
        """
        return self.__base_post(self.url, ['write_checkouts'], data)

    def retrieve(self, checkout_id):
        """Retrieve a checkout.\n
        Scopes: 'read_checkouts'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/checkouts/checkout_retrieve>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/checkouts/checkout_retrieve>`_
        """
        return self.__base_get(f'{self.url}/{checkout_id}', ['read_checkouts'])

    def update(self, checkout_id, data):
        """Update a checkout.\n
        Scopes: 'write_checkouts'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/checkouts/checkout_update>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/checkouts/checkout_update>`_
        """
        return self.__base_put(f'{self.url}/{checkout_id}', ['write_checkouts'],
                               data)

    def get_shipping(self, checkout_id):
        """Retrieve shipping rates for a checkout.\n
        Scopes: 'read_checkouts'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/checkouts/checkout_retrieve_shipping_address>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/checkouts/checkout_retrieve_shipping_address>`_
        """
        return self.__base_get(f'{self.url}/{checkout_id}/shipping_rates',
                               ['read_checkouts'])

    def charge(self, checkout_id, data):
        """Process (charge) a checkout.\n
        Scopes: 'write_checkouts'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/checkouts/checkout_process>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-01/checkouts/checkout_process>`_
        """
        return self.__base_post(f'{self.url}/{checkout_id}/charge',
                                ['write_checkouts'], data)
