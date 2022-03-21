from recharge.base import RechargeResource
from recharge.decorators import recharge_v1, recharge_v2


class RechargeCharge(RechargeResource):
    """
    https://developer.rechargepayments.com/#charges
    """
    object_list_key = 'charges'

    def retrieve(self, resource_id):
        """Retrieve a charge.
        https://developer.rechargepayments.com/2021-01/charges/charge_retrieve
        """
        return self.__base_get(f'{self.url}/{resource_id}')

    def list(self, data=None):
        """List charges
        https://developer.rechargepayments.com/2021-01/charges
        """
        return self.__base_get(self.url, data)

    def skip(self, charge_id, subscription_id):
        """Skip a charge.
        https://developer.rechargepayments.com/v1#skip-a-charge
        """
        return self.__base_post(
            f'{self.url}/{charge_id}/skip',
            {"subscription_id": subscription_id}
        )

    def unskip(self, charge_id, subscription_id):
        """Unskip a charge.
        https://developer.rechargepayments.com/v1#unskip-a-charge
        """
        return self.__base_post(
            f'{self.url}/{charge_id}/unskip',
            {"subscription_id": subscription_id}
        )

    def refund(self, charge_id, amount):
        """Refund a charge.
        https://developer.rechargepayments.com/v1#refund-a-charge
        """
        return self.__base_post(
            f'{self.url}/{charge_id}/refund',
            {"amount": amount}
        )

    def full_refund(self, charge_id):
        """Full refund a charge
        https://developer.rechargepayments.com/v1#full-refund-a-charge
        """
        return self.__base_post(
            f'{self.url}/{charge_id}/refund',
            {"full_refund": True}
        )

    def process(self, charge_id):
        """Process a charge.
        https://developer.rechargepayments.com/v1#process-a-charge
        """
        return self.__base_post(
            f'{self.url}/{charge_id}/process',
            {}
        )

    @recharge_v1
    def count(self, data=None):
        """Retrieve a count of charges.
        https://developer.rechargepayments.com/v1#count-charges
        """
        return self.__base_get(f'{self.url}/count', data)

    @recharge_v1
    def change_next_charge_date(self, charge_id, next_charge_date):
        """Change next charge date
        https://developer.rechargepayments.com/2021-01/charges/charge_change_next_date
        """
        return self.__base_post(
                f'{self.url}/{charge_id}/change_next_charge_date',
                {'next_charge_date': next_charge_date}
        )

    @recharge_v2
    def apply_discount(self, charge_id, data):
        """Apply a discount to a queued charge.
        https://developer.rechargepayments.com/2021-11/charges/apply_discount
        """
        return self.__base_post(f'{self.url}/{charge_id}/apply_discount', data)

    @recharge_v2
    def remove_discount(self, charge_id, data):
        """Remove a discount to a queued charge.
        https://developer.rechargepayments.com/2021-11/charges/apply_discount
        """
        return self.__base_post(f'{self.url}/{charge_id}/remove_discount', data)
