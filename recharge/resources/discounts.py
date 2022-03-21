from recharge.base import RechargeResource
from recharge.decorators import recharge_v1, recharge_v2

class RechargeDiscount(RechargeResource):
    """
    https://developer.rechargepayments.com/#discounts
    """
    object_list_key = 'discounts'

    def create(self, data):
        return self.__base_post(self.url, data)

    def retrieve(self, resource_id):
        return self.__base_get(f'{self.url}/{resource_id}')

    def update(self, resource_id, data):
        return self.__base_put(f'{self.url}/{resource_id}', data)

    def delete(self, discount_id):
        """Delete a Discount
        https://developer.rechargepayments.com/#delete-a-discount
        """
        return self.__base_delete(f'{self.url}/{discount_id}')

    def list(self, data=None):
        return self.__base_get(self.url, data)

    @recharge_v1
    def count(self, data=None):
        """Receive a count of all discounts.
        https://developer.rechargepayments.com/v1#count-discounts
        """
        return self.__base_get(f'{self.url}/count', data)

    @recharge_v1
    def apply(self, resource, resource_id, discount_code):
        """Apply a discount to an address or charge.
        https://developer.rechargepayments.com/v1#apply-a-discount-to-an-address
        """
        if resource not in ['addresses', 'charges']:
            raise ValueError("Resource is not 'addresses' or 'charges'")
        return self.__base_post(
            f'{self.base_url}/{resource}/{resource_id}/apply_discount',
            {"discount_code": discount_code}
        )

    @recharge_v1
    def remove(self, resource, resource_id):
        """Remove a discount from a charge or address without destroying the discount.
        https://developer.rechargepayments.com/v1#remove-a-discount
        """
        if resource not in ['addresses', 'charges']:
            raise ValueError("Resource is not 'addresses' or 'charges'.")
        return self.__base_post(
            f'{self.base_url}/{resource}/{resource_id}/remove_discount',
            {}
        )