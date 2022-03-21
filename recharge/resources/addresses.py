from recharge.base import RechargeResource
from recharge.decorators import recharge_v1


class RechargeAddress(RechargeResource):
    """
    https://developer.rechargepayments.com/#addresses
    """
    object_list_key = 'addresses'

    def create(self, customer_id, data):
        """Create an address for the customer.
        https://developer.rechargepayments.com/#create-address
        """
        url = f'{self.base_url}/customers/{customer_id}/{self.object_list_key}'
        return self.__base_post(url, data)

    def retrieve(self, resource_id):
        """Retrieve an address.
        https://developer.rechargepayments.com/2021-01/addresses/retrieve_address
        """
        return self.__base_get(f'{self.url}/{resource_id}')

    def update(self, resource_id, data):
        """Update an address.
        https://developer.rechargepayments.com/2021-11/addresses/update_address
        """
        return self.__base_put(f'{self.url}/{resource_id}', data)

    def delete(self, address_id):
        """Delete an address.
        https://developer.rechargepayments.com/v1#delete-an-address
        """
        return self.__base_delete(f'{self.url}/{address_id}')

    def list(self, data=None):
        """List addresses.
        https://developer.rechargepayments.com/2021-11/addresses/list_addresses
        """
        return self.__base_get(self.url, data)

    @recharge_v1
    def apply_discount(self, address_id, discount_code):
        """ Apply a discount code to an address.
        https://developer.rechargepayments.com/#add-discount-to-address-new
        """
        return self.__base_post(
            f'{self.url}/{address_id}/apply_discount',
            {'discount_code': discount_code}
        )

    @recharge_v1
    def validate_address(self, data):
        """Validate an address, only works for USA Addresses.
        https://developer.rechargepayments.com/2021-01/addresses/validate_address
        """
        return self.__base_post(f'{self.url}/validate', data)

    @recharge_v1
    def count(self, data=None):
        """Retrieve the count of addresses.
        https://developer.rechargepayments.com/v1#count-addresses
        """
        return self.__base_get(f'{self.url}/count', data)
