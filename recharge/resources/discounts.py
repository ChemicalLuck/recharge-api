from recharge.base import RechargeResource
from recharge.decorators import recharge_v1


class RechargeDiscount(RechargeResource):
    """
    `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/discounts>`_\n
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/discounts>`_
    """
    object_key = 'discounts'

    def create(self, data):
        """Create a new discount.\n
        Scopes: 'write_discounts'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/discounts/discounts_create>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/discounts/discounts_create>`_'
        """
        return self.__base_post(self.url, ['write_discounts'], data)

    def retrieve(self, resource_id):
        """Retrieve a discount.\n
        Scopes: 'read_discounts'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/discounts/discounts_retrieve>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/discounts/discounts_retrieve>`_
        """
        return self.__base_get(f'{self.url}/{resource_id}', ['read_discounts'])

    def update(self, resource_id, data):
        """Update a discount.\n
        Scopes: 'write_discounts'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/discounts/discounts_update>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/discounts/discounts_update>`_
        """
        return self.__base_put(f'{self.url}/{resource_id}', ['write_discounts'],
                               data)

    def delete(self, discount_id):
        """Delete a Discount.\n
        Scopes: 'write_discounts'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/discounts/discounts_delete>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-01/discounts/discounts_delete>`_
        """
        return self.__base_delete(f'{self.url}/{discount_id}',
                                  ['write_discounts'])

    def list(self, data=None):
        """List discounts.\n
        Scopes: 'read_discounts'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/discounts/discounts_list>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/discounts/discounts_list>`_"""
        return self.__base_get(self.url, ['read_discounts'], data)

    @recharge_v1
    def count(self, data=None):
        """Receive a count of all discounts.\n
        Scopes: 'read_discounts'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/discounts/discounts_count>`_
        """
        return self.__base_get(f'{self.url}/count', ['read_discounts'], data)

    @recharge_v1
    def apply(self, resource, resource_id, discount_code):
        """Apply a discount to an address or charge.\n
        Scopes: 'write_discounts', 'write_customers', 'write_orders'\n
        `v1/2021-01 Address Docs <https://developer.rechargepayments.com/2021-01/discounts/discounts_apply_address>`_\n
        `v1/2021-01 Charge Docs <https://developer.rechargepayments.com/2021-01/discounts/discounts_apply_charge>`_
        """
        if resource not in ['addresses', 'charges']:
            raise ValueError("Resource is not 'addresses' or 'charges'")
        return self.__base_post(
            f'{self.base_url}/{resource}/{resource_id}/apply_discount',
            ['write_discounts', 'write_customers', 'write_orders'],
            {"discount_code": discount_code})

    @recharge_v1
    def remove(self, resource, resource_id):
        """Remove a discount from a charge or address without destroying the discount.\n
        Scopes: 'write_discounts', 'write_customers', 'write_orders'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/discounts/discounts_remove_from_address_or_charge>`_
        """
        if resource not in ['addresses', 'charges']:
            raise ValueError("Resource is not 'addresses' or 'charges'.")
        return self.__base_post(
            f'{self.base_url}/{resource}/{resource_id}/remove_discount',
            ['write_discounts', 'write_customers', 'write_orders'], {})
