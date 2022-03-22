from recharge.base import RechargeResource
from recharge.decorators import recharge_v2


class RechargePlan(RechargeResource):
    """
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/plans>`_\n
    """
    object_key = 'plans'

    @recharge_v2
    def create(self, data):
        """Create a plan.\n
        Scopes: 'write_products'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/plans/plans_create>`_
        """
        self.__check_scopes(['write_products'])
        return self.__base_post(self.url, data)

    @recharge_v2
    def update(self, plan_id, data):
        """Update a plan.\n
        Scopes: 'write_products'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/plans/plans_update>`_
        """
        self.__check_scopes(['write_products'])
        return self.__base_put(f'{self.url}/{plan_id}', data)

    @recharge_v2
    def delete(self, plan_id):
        """Delete a plan.\n
        Scopes: 'write_products'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/plans/plans_delete>`_
        """
        self.__check_scopes(['write_products'])
        return self.__base_delete(f'{self.url}/{plan_id}')

    @recharge_v2
    def list(self, data):
        """List plans.\n
        Scopes: 'read_products'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/plans/plans_list>`_
        """
        self.__check_scopes(['read_products'])
        return self.__base_get(self.url, data)
