from recharge.base import RechargeResource
from recharge.decorators import recharge_v1


class RechargeMetafield(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/metafields
    """
    object_key = 'metafields'

    def create(self, data):
        """Create a metafield.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_create
        """
        return self.__base_post(self.url, data)

    def retrieve(self, metafield_id):
        """Retrieve a metafield.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_retrieve
        """
        return self.__base_get(f'{self.url}/{metafield_id}')

    def update(self, metafield_id, data):
        """Update a metafield.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_update
        """
        return self.__base_put(f'{self.url}/{metafield_id}', data)

    def delete(self, metafield_id):
        """Delete a metafield.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_delete
        """
        return self.__base_delete(f'{self.url}/{metafield_id}')

    def list(self, data=None):
        """List metafields.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_list
        """
        return self.__base_get(self.url, data)

    @recharge_v1
    def count(self, data=None):
        """Count metafields.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_count
        """
        return self.__base_get(f'{self.url}/count', data)
