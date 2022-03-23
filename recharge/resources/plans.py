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
        return self.__base_post(self.url, ['write_products'], data)

    @recharge_v2
    def update(self, plan_id, data):
        """Update a plan.\n
        Scopes: 'write_products'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/plans/plans_update>`_
        """
        return self.__base_put(f'{self.url}/{plan_id}', ['write_products'],
                               data)

    @recharge_v2
    def delete(self, plan_id):
        """Delete a plan.\n
        Scopes: 'write_products'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/plans/plans_delete>`_
        """
        return self.__base_delete(f'{self.url}/{plan_id}', ['write_products'])

    @recharge_v2
    def list(self, data):
        """List plans.\n
        Scopes: 'read_products'\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/plans/plans_list>`_
        """
        return self.__base_get(self.url, ['read_products'], data)
