from recharge.base import RechargeResource
from recharge.decorators import recharge_v1, recharge_v2


class RechargeShop(RechargeResource):
    """
    `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/shop>`_
    """
    object_key = 'shop'

    @recharge_v1
    def retrieve(self, data=None):
        """Retrieve a shop.\n
        Scopes: 'read_store', 'read_shop', 'store_info'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/shop/shop_retrieve>`_
        """
        self.__check_scopes(['read_store', 'read_shop', 'store_info'])
        object_key = 'shop' if self.version == '2021-01' else 'store'
        return self.__base_get(f"{self.base_url}/{object_key}", data)

    @recharge_v1
    def retrieve_shipping_countries(self, data=None):
        """Retrieve shipping countries.\n
        Scopes: 'read_store', 'read_shop', 'store_info'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/shop/shop_shipping_countries>`_
        """
        self.__check_scopes(['read_store', 'read_shop', 'store_info'])
        return self.__base_get(f'{self.url}/shipping_countries', data)


class RechargeStore(RechargeResource):
    """
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/store>`_
    """
    object_key = 'store'

    @recharge_v2
    def retrieve(self, data=None):
        """Retrieve a store.\n
        Scopes: 'read_store', 'store_info'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/store/store_retrieve>`_
        """
        self.__check_scopes(['read_store', 'store_info'])
        return self.__base_get(self.url, data)
