from recharge.base import RechargeResource
from recharge.decorators import recharge_v2


class RechargePaymentMethod(RechargeResource):
    """
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/payment_methods>`_
    """
    object_key = 'payment_methods'

    @recharge_v2
    def create(self, data):
        """Create a payment method.\n
        Scopes: 'write_payment_methods'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_create>`_
        """
        self.__check_scopes(['write_payment_methods'])
        return self.__base_post(self.url, data)

    @recharge_v2
    def retrieve(self, payment_method_id):
        """Retrieve a payment method.\n
        Scopes: 'write_payment_methods'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_retrieve>`_
        """
        self.__check_scopes(['read_payment_methods'])
        return self.__base_get(f'{self.url}/{payment_method_id}')

    @recharge_v2
    def update(self, payment_method_id, data):
        """Update a payment method.\n
        Scopes: 'write_payment_methods'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_update>`_
        """
        self.__check_scopes(['write_payment_methods'])
        return self.__base_put(f'{self.url}/{payment_method_id}', data)

    @recharge_v2
    def delete(self, payment_method_id):
        """Delete a payment method.\n
        Scopes: 'write_payment_methods'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_delete>`_
        """
        self.__check_scopes(['write_payment_methods'])
        return self.__base_delete(f'{self.url}/{payment_method_id}')

    @recharge_v2
    def list(self, data):
        """List payment methods.\n
        Scopes: 'write_payment_methods'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_list>`_
        """
        self.__check_scopes(['read_payment_methods'])
        return self.__base_get(self.url, data)