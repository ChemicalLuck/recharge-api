from recharge.base import RechargeResource
from recharge.decorators import recharge_v1


class RechargeOrder(RechargeResource):
    """
    `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/orders>`_\n
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/orders>`_
    """
    object_key = 'orders'

    def retrieve(self, order_id):
        """Retrieve an order.\n
        Scopes: 'read_orders'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/orders_retrieve>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/orders_retrieve>`_
        """
        return self.__base_get(f'{self.url}/{order_id}', ['read_orders'])

    def update(self, order_id, data):
        """Update an order.\n
        Scopes: 'write_orders'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/orders_update>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/orders_update>`_
        """
        return self.__base_put(f'{self.url}/{order_id}', ['write_orders'], data)

    def delete(self, order_id):
        """Delete an order.\n
        Scopes: 'write_orders'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/orders_delete>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/orders_delete>`_
        """
        return self.__base_delete(f'{self.url}/{order_id}', ['write_orders'])

    def list(self, data=None):
        """List orders.\n
        Scopes: 'read_orders'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/orders_list>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/orders_list>`_
        """
        return self.__base_get(self.url, ['read_orders'], data)

    def clone(self, order_id, charge_id, data):
        """Clone an order on charge success.\n
        Scopes: 'write_orders'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/orders_clone>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/orders_clone>`_
        """
        return self.__base_post(
            f'{self.url}/clone_order_on_success_charge/{order_id}/charge/{charge_id}',
            ['write_orders'], data)

    @recharge_v1
    def count(self, data=None):
        """Count orders.\n
        Scopes: 'read_orders'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/orders/orders_change_date>`_
        """
        return self.__base_get(f'{self.url}/count', ['read_orders'], data)

    @recharge_v1
    def change_order_date(self, order_id, new_date):
        """Change an order date.\n
        Scopes: 'write_orders'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/orders/orders_change_dates>`_
        """
        return self.__base_post(f'{self.url}/{order_id}/change_date',
                                ['write_orders'], {'scheduled_at': new_date})

    @recharge_v1
    def change_an_order_variant(self, order_id, old_variant_id, new_variant_id):
        """Change an order variant.\n
        Scopes: 'write_orders'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/orders_change_variant>`_
        """
        return self.__base_put(
            f'{self.url}/{order_id}/update_shopify_variant/{old_variant_id}',
            ['write_orders'], {'new_shopify_variant_id': new_variant_id})
