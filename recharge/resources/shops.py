from recharge.base import RechargeResource
from recharge.decorators import recharge_v1


class RechargeShop(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/shop
    """
    object_key = 'shop'

    def retrieve(self, data=None):
        """Retrieve a shop.
        https://developer.rechargepayments.com/2021-01/shop/shop_retrieve
        """
        return self.__base_get(self.url, data)

    @recharge_v1
    def retrieve_shipping_countries(self, data=None):
        """Retrieve shipping countries.
        https://developer.rechargepayments.com/2021-01/shop/shop_shipping_countries
        """
        return self.__base_get(f'{self.url}/shipping_countries', data)
