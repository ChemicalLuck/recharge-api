from recharge.base import RechargeResource


class RechargeNotification(RechargeResource):
    """
    `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/notifications>`_\n
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/notifications>`_
    """
    object_key = 'notifications'

    def send(self, customer_id, data):
        """Send an email notification.\n
        Scopes: 'write_notifications'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/notifications/notifications_get_account_access>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/notifications/notifications_send>`_
        """
        self.__check_scopes(['write_notifications'])
        return self.__base_post(
                f'{self.base_url}/customers/{customer_id}/{self.object_key}',
                data
        )