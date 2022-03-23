from recharge.base import RechargeResource
from recharge.decorators import recharge_v1, recharge_v2


class RechargeCustomer(RechargeResource):
    """
    `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/customers>`_\n
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/customers>`_
    """
    object_key = 'customers'

    def create(self, data):
        """Create a customer.\n
        Scopes: 'write_customers', 'write_payments'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/customers/customers_create>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/customers/customers_create>`_
        """
        return self.__base_post(self.url, ['write_customers', 'write_payments'],
                                data)

    def retrieve(self, customer_id):
        """Retrieve a customer.\n
        Scopes: 'read_customers'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/customers/customers_retrieve>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/customers/customers_retrieve>`_
        """
        return self.__base_get(f'{self.url}/{customer_id}', ['read_customers'])

    def update(self, customer_id, data):
        """Update a customer.\n
        Scopes: 'write_customers'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/customers/customers_update>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/customers/customers_update>`_
        """
        return self.__base_put(f'{self.url}/{customer_id}', ['write_customers'],
                               data)

    def delete(self, customer_id):
        """Delete a customer.\n
        Scopes: 'write_customers'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/customers/customers_delete>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/customers/customers_delete>`_
        """
        return self.__base_delete(f'{self.url}/{customer_id}',
                                  ['write_customers'])

    def list(self, data=None):
        """List customers.\n
        Scopes: 'read_customers'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/customers/customers_list>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/customers/customers_list>`_
        """
        return self.__base_get(self.url, ['read_customers'], data)

    @recharge_v1
    def count(self, data=None):
        """Retrieve a count of customers.\n
        Scopes: 'read_customers'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/customers/customers_count>`_
        """
        return self.__base_get(f'{self.url}/count', ['read_customers'], data)

    @recharge_v2
    def retrieve_delivery_schedule(self, customer_id, data=None):
        """Retrieve a list of projected deliveries in a specific interval.\n
        Scopes: 'read_customers'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/customers/customer_delivery_schedule>`_
        """
        return self.__base_get(f'{self.url}/{customer_id}/deivery_schedule',
                               ['read_customers'], data)

    @recharge_v1
    def retrieve_payment_sources(self, customer_id, data=None):
        """Retrieve payment sources for customer.\n
        Scopes: 'read_customers'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/customers/customers_payment_source>`_
        """
        return self.__base_get(f'{self.url}/{customer_id}/payment_sources',
                               ['read_customers'], data)
