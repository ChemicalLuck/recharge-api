from recharge.base import RechargeResource
from recharge.decorators import recharge_v1


class RechargeSubscription(RechargeResource):
    """

    """
    object_key = 'subscriptions'

    def create(self, data):
        """Create a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_create
        """
        return self.__base_post(self.url, data)

    def retrieve(self, subscription_id):
        """Retrieve a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_retrieve
        """
        return self.__base_get(f'{self.url}/{subscription_id}')

    def update(self, subscription_id, data):
        """Update a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_update
        """
        return self.__base_put(f'{self.url}/{subscription_id}', data)

    def delete(self, subscription_id):
        """Delete a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_delete
        """
        return self.__base_delete(f'{self.url}/{subscription_id}')

    def list(self, data=None):
        """List subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_list
        """
        return self.__base_get(self.url, data)

    @recharge_v1
    def count(self, data=None):
        """Count subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_count
        """
        return self.__base_get(f'{self.url}/count', data)

    def set_next_charge_date(self, subscription_id, date):
        """Change the next charge date of a subscription
        https://developer.rechargepayments.com/#change-next-charge-date-on-subscription
        """
        return self.__base_post(
            f'{self.url}/{subscription_id}/set_next_charge_date',
            {'date': date}
        )

    def change_address(self, subscription_id, address_id):
        """Change a subscription address.
        https://developer.rechargepayments.com/v1#change-a-subscription-address
        """
        return self.__base_post(
            f'{self.url}/{subscription_id}/change_address',
            {"address_id": address_id}
        )

    def cancel(self, subscription_id, data=None):
        """Cancel a subscription.
        https://developer.rechargepayments.com/#cancel-subscription
        """
        return self.__base_post(f'{self.url}/{subscription_id}/cancel', data)

    def activate(self, subscription_id):
        """Activate a cancelled subscription.
        https://developer.rechargepayments.com/v1#activate-a-subscription
        """
        return self.__base_post(f'{self.url}/{subscription_id}/activate', {})

    @recharge_v1
    def create_bulk(self, address_id, data):
        """Bulk create subscriptions for address.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_create
        """
        return self.__base_post(
            f'{self.base_url}/addresses/{address_id}/subscriptions-bulk',
            data
        )

    @recharge_v1
    def update_bulk(self, address_id, data):
        """Bulk update subscriptions for address.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_update
        """
        return self.__base_put(
            f'{self.base_url}/addresses/{address_id}/subscriptions-bulk',
            data
        )

    @recharge_v1
    def delete_bulk(self, address_id, data):
        """Bulk delete subscriptions for address.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_delete
        """
        return self.__base_delete(
            f'{self.base_url}/addresses/{address_id}/subscriptions-bulk',
            data
        )
