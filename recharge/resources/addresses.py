from recharge.base import RechargeResource
from recharge.decorators import recharge_v1


class RechargeAddress(RechargeResource):
    """
    `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/addresses>`_\n
    `v2/2021-11 Docs <https://developer.rechargepayments.com/2021-11/addresses>`_
    """
    object_key = 'addresses'

    def create(self, customer_id, data):
        """Create an address for the customer.\n
        Scopes: 'write_customers'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/addresses/create_address>`_\n
        `v2/2021-11 Docs <https://developer.rechargepayments.com/2021-11/addresses/create_address>`_
        """
        self.__check_scopes(['write_customers'])
        url = f'{self.base_url}/customers/{customer_id}/{self.object_key}'
        return self.__base_post(url, data)

    def retrieve(self, resource_id):
        """Retrieve an address.\n
        Scopes: 'read_customers'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/addresses/retrieve_address>`_\n
        `v2/2021-11 Docs <https://developer.rechargepayments.com/2021-11/addresses/retrieve_address>`_
        """
        self.__check_scopes(['read_customers'])
        return self.__base_get(f'{self.url}/{resource_id}')

    def update(self, resource_id, data):
        """Update an address.\n
        Scopes: 'write_customers'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/addresses/update_address>`_\n
        `v2/2021-11 Docs <https://developer.rechargepayments.com/2021-11/addresses/update_address>`_
        """
        self.__check_scopes(['write_customers'])
        return self.__base_put(f'{self.url}/{resource_id}', data)

    def delete(self, address_id):
        """Delete an address.\n
        Scopes: 'write_customers'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/addresses/delete_address>`_\n
        `v2/2021-11 Docs <https://developer.rechargepayments.com/2021-11/addresses/delete_address>`_
        """
        self.__check_scopes(['write_customers'])
        return self.__base_delete(f'{self.url}/{address_id}')

    def list(self, data=None):
        """List addresses.\n
        Scopes: 'read_customers'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/addresses/list_addresses>`_\n
        `v2/2021-11 Docs <https://developer.rechargepayments.com/2021-11/addresses/list_addresses>`_
        """
        self.__check_scopes(['read_customers'])
        return self.__base_get(self.url, data)

    @recharge_v1
    def validate_address(self, data):
        """Validate an address, only works for USA Addresses.\n
        Scopes: None\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/addresses/validate_address>`_
        """
        return self.__base_post(f'{self.url}/validate', data)

    @recharge_v1
    def count(self, data=None):
        """Retrieve the count of addresses.\n
        Scopes: 'read_customers'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/addresses/count_addresses>`_
        """
        self.__check_scopes(['read_customers'])
        return self.__base_get(f'{self.url}/count', data)
