from recharge.base import RechargeResource
from recharge.decorators import recharge_v1, recharge_v2


class RechargeCustomer(RechargeResource):
    """
    https://developer.rechargepayments.com/#customers
    """
    object_list_key = 'customers'

    def create(self, data):
        """Create a customer.
        https://developer.rechargepayments.com/2021-01/customers/customers_create
        """
        return self.__base_post(self.url, data)

    def retrieve(self, customer_id):
        """Retrieve a customer.
        https://developer.rechargepayments.com/2021-01/customers/customers_retrieve
        """
        return self.__base_get(f'{self.url}/{customer_id}')

    def update(self, customer_id, data):
        """Update a customer.
        https://developer.rechargepayments.com/2021-01/customers/customers_update
        """
        return self.__base_put(f'{self.url}/{customer_id}', data)

    def delete(self, customer_id):
        """Delete a customer.
        https://developer.rechargepayments.com/v1#delete-a-customer
        """
        return self.__base_delete(f'{self.url}/{customer_id}')

    def list(self, data=None):
        """List customers.
        https://developer.rechargepayments.com/2021-01/customers/customers_list
        """
        return self.__base_get(self.url, data)

    @recharge_v1
    def count(self, data=None):
        """Retrieve a count of customers.
        https://developer.rechargepayments.com/v1#count-customers
        """
        return self.__base_get(f'{self.url}/count', data)

    @recharge_v2
    def retrieve_delivery_schedule(self, customer_id, data):
        """Retrieve a list of projected deliveries in a specific interval.
        https://developer.rechargepayments.com/2021-11/customers/customer_delivery_schedule
        """
        return self.__base_get(f'{self.url}/{customer_id}/deivery_schedule', data)
