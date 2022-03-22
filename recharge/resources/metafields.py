from recharge.base import RechargeResource
from recharge.decorators import recharge_v1


class RechargeMetafield(RechargeResource):
    """
    `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/metafields>`_\n
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/metafields>`_
    """
    object_key = 'metafields'

    def create(self, data):
        """Create a metafield.\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/metafields/metafields_create>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/metafields/metafields_create>`_
        """
        return self.__base_post(self.url, data)

    def retrieve(self, metafield_id):
        """Retrieve a metafield.
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/metafields/metafields_retrieve>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/metafields/metafields_retrieve>`_
        """
        return self.__base_get(f'{self.url}/{metafield_id}')

    def update(self, metafield_id, data):
        """Update a metafield.
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/metafields/metafields_update>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/metafields/metafields_update>`_
        """
        return self.__base_put(f'{self.url}/{metafield_id}', data)

    def delete(self, metafield_id):
        """Delete a metafield.
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/metafields/metafields_delete>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/metafields/metafields_delete>`_
        """
        return self.__base_delete(f'{self.url}/{metafield_id}')

    def list(self, data=None):
        """List metafields.
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/metafields/metafields_list>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/metafields/metafields_list>`_
        """
        return self.__base_get(self.url, data)

    @recharge_v1
    def count(self, data=None):
        """Count metafields.
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/metafields/metafields_count>`_
        """
        return self.__base_get(f'{self.url}/count', data)
