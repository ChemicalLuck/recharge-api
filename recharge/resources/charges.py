from recharge.base import RechargeResource
from recharge.decorators import recharge_v1, recharge_v2


class RechargeCharge(RechargeResource):
    """
    `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/charges>`_\n
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/charges>`_
    """
    object_key = 'charges'

    def retrieve(self, charge_id):
        """Retrieve a charge.\n
        Scopes: 'read_orders'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/charges/charge_retrieve>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/charges/charge_retrieve>`_
        """
        return self.__base_get(f'{self.url}/{charge_id}', ['read_orders'])

    def list(self, data=None):
        """List charges.\n
        Scopes: 'read_orders'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/charges/charge_list>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/charges/charge_list>`_
        """
        return self.__base_get(self.url, ['read_orders'], data)

    @recharge_v1
    def count(self, data=None):
        """Retrieve a count of charges.\n
        Scopes: 'read_orders'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/charges/charge_count>`_
        """
        return self.__base_get(f'{self.url}/count', ['read_orders'], data)

    @recharge_v1
    def change_next_charge_date(self, charge_id, next_charge_date):
        """Change next charge date.\n
        Scopes: 'write_orders'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/charges/charge_change_next_date>`_
        """
        return self.__base_post(
                f'{self.url}/{charge_id}/change_next_charge_date',
                ['write_orders'], {'next_charge_date': next_charge_date})

    def skip(self, charge_id, subscription_id):
        """Skip a charge.\n
        Scopes: 'write_orders'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/charges/charge_skip>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/charges/charge_skip>`_
        """
        return self.__base_post(f'{self.url}/{charge_id}/skip',
                                ['write_orders'],
                                {"subscription_id": subscription_id})

    def unskip(self, charge_id, subscription_id):
        """Unskip a charge.\n
        Scopes: 'write_orders'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/charges/charge_unskip>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/charges/charge_unskip>`_
        """
        return self.__base_post(f'{self.url}/{charge_id}/unskip',
                                ['write_orders'],
                                {"subscription_id": subscription_id})

    def refund(self, charge_id, amount):
        """Refund a charge.\n
        Scopes: 'write_orders', 'write_payments'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/charges/charge_refund>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/charges/charge_refund>`_
        """
        return self.__base_post(f'{self.url}/{charge_id}/refund',
                                ['write_orders', 'write_payments'],
                                {"amount": amount})

    def full_refund(self, charge_id):
        """Full refund a charge.\n
        Scopes: 'write_orders', 'write_payments'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/charges/charge_refund>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/charges/charge_refund>`_
        """
        return self.__base_post(f'{self.url}/{charge_id}/refund',
                                ['write_orders', 'write_payments'],
                                {"full_refund": True})

    def process(self, charge_id):
        """Process a charge.\n
        Scopes: 'process_charges'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/charges/charge_process>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/charges/charge_process>`_
        """
        return self.__base_post(f'{self.url}/{charge_id}/process',
                                ['process_charges'], {})

    @recharge_v2
    def apply_discount(self, charge_id, data):
        """Apply a discount to a queued charge.\n
        Scopes: 'write_orders'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/charges/apply_discount>`_
        """
        return self.__base_post(f'{self.url}/{charge_id}/apply_discount',
                                ['write_orders'], data)

    @recharge_v2
    def remove_discount(self, charge_id, data):
        """Remove a discount to a queued charge.\n
        Scopes: 'write_orders'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/charges/remove_discount>`_
        """
        return self.__base_post(f'{self.url}/{charge_id}/remove_discount',
                                ['write_orders'], data)
