from recharge.base import RechargeResource
from recharge.decorators import recharge_v2


class RechargeAccount(RechargeResource):
    """
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/accounts>`_
    """
    object_key = 'accounts'

    @recharge_v2
    def retrieve(self, account_id):
        """Retrieve an account.\n
        Scopes: 'read_accounts'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/accounts/account_retrieve>`_
        """
        self.__base_get(f'{self.url}/{account_id}', {})

    @recharge_v2
    def list(self):
        """List accounts.\n
        Scopes: 'read_accounts'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/accounts/accounts_list>`_
        """