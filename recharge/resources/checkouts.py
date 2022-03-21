from recharge.base import RechargeResource


class RechargeCheckout(RechargeResource):
    """
    https://developer.rechargepayments.com/#checkouts
    """
    object_key = 'checkouts'

    def create(self, data):
        """Create a checkout
        https://developer.rechargepayments.com/2021-01/checkouts
        """
        return self.__base_post(self.url, data)

    def retrieve(self, checkout_id):
        """Retrieve a checkout.
        https://developer.rechargepayments.com/2021-01/checkouts/checkout_retrieve
        """
        return self.__base_get(f'{self.url}/{checkout_id}')

    def update(self, checkout_id, data):
        """Update a checkout.
        https://developer.rechargepayments.com/2021-01/checkouts/checkout_update
        """
        return self.__base_put(f'{self.url}/{checkout_id}', data)

    def get_shipping(self, checkout_id):
        """Retrieve shipping rates for a checkout
        https://developer.rechargepayments.com/v1#retrieve-shipping-rates-for-a-checkout
        """
        return self.__base_get(f'{self.url}/{checkout_id}/shipping_rates')

    def charge(self, checkout_id, data):
        """Process (charge) a checkout.
        https://developer.rechargepayments.com/#process-checkout-beta
        """
        return self.__base_post(f'{self.url}/{checkout_id}/charge', data)
