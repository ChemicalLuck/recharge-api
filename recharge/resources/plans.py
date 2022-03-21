from recharge.base import RechargeResource
from recharge.decorators import recharge_v2


class RechargePlan(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/plans
    """
    object_key = 'plans'

    @recharge_v2
    def create(self, data):
        """Create a plan.
        https://developer.rechargepayments.com/2021-11/plans/plans_create
        """
        return self.__base_post(self.url, data)

    @recharge_v2
    def update(self, plan_id, data):
        """Update a plan.
        https://developer.rechargepayments.com/2021-11/plans/plans_update
        """
        return self.__base_put(f'{self.url}/{plan_id}', data)

    @recharge_v2
    def delete(self, plan_id):
        """Delete a plan.
        https://developer.rechargepayments.com/2021-11/plans/plans_delete
        """
        return self.__base_delete(f'{self.url}/{plan_id}')

    @recharge_v2
    def list(self, data):
        """List plans.
        https://developer.rechargepayments.com/2021-11/plans/plans_list
        """
        return self.__base_get(self.url, data)
