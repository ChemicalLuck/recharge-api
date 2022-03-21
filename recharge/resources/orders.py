from recharge.base import RechargeResource
from recharge.decorators import recharge_v1


class RechargeOrder(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/orders
    """
    object_key = 'orders'

    def retrieve(self, order_id):
        """Retrieve an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_retrieve
        """
        return self.__base_get(f'{self.url}/{order_id}')

    def update(self, order_id, data):
        """Update an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_update
        """
        return self.__base_put(f'{self.url}/{order_id}', data)

    def delete(self, order_id):
        """Delete an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_delete
        """
        return self.__base_delete(f'{self.url}/{order_id}')

    def list(self, data=None):
        """List an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_list
        """
        return self.__base_get(self.url, data)

    def clone(self, order_id, charge_id, data):
        """Clone an order on charge success.
        https://developer.rechargepayments.com/2021-01/orders/orders_clone
        """
        return self.__base_post(
            f'{self.url}/clone_order_on_success_charge/{order_id}/charge/{charge_id}',
            data
        )

    @recharge_v1
    def count(self, data=None):
        """Count orders.
        https://developer.rechargepayments.com/2021-01/orders/orders_count
        """
        return self.__base_get(f'{self.url}/count', data)

    @recharge_v1
    def change_order_date(self, order_id, new_date):
        """Change an order date.
        https://developer.rechargepayments.com/2021-01/orders/orders_change_date
        """
        return self.__base_post(
            f'{self.url}/{order_id}/change_date',
                {'scheduled_at': new_date}
    )

    @recharge_v1
    def change_an_order_variant(self, order_id, old_variant_id, new_variant_id):
        """Change an order variant.
        https://developer.rechargepayments.com/2021-01/orders/orders_change_variant
        """
        return self.__base_put(
            f'{self.url}/{order_id}/update_shopify_variant/{old_variant_id}',
            {'new_shopify_variant_id': new_variant_id}
        )
