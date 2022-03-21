from recharge.base import RechargeResource


class RechargeNotification(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/notifications
    """

    def send(self, customer_id, data):
        """Send an email notification.
        https://developer.rechargepayments.com/2021-01/notifications/notifications_get_account_access
        """
        return self.__base_post(
                f'{self.base_url}/customers/{customer_id}/notifications',
                data
        )