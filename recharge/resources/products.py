from recharge.base import RechargeResource
from recharge.decorators import recharge_v1


class RechargeProduct(RechargeResource):
    """
    `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/products>`_\n
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/products>`_
    """
    object_key = 'products'

    def create(self, data):
        """Create a product.\n
        Scopes: 'write_products'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/products/products_create>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/products/products_create>`_
        """
        return self.__base_post(self.url, ['write_products'], data)

    def retrieve(self, product_id):
        """Retrieve a product.\n
        Scopes: 'write_products'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/products/products_retrieve>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/products/products_retrieve>`_
        """
        return self.__base_get(f'{self.url}/{product_id}', ['read_products'])

    def update(self, product_id, data):
        """Update a product.\n
        Scopes: 'write_products'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/products/products_update>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/products/products_update>`_
        """
        return self.__base_put(f'{self.url}/{product_id}', ['write_products'],
                               data)

    def delete(self, product_id):
        """Delete a product.\n
        Scopes: 'write_products'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/products/products_delete>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/products/products_delete>`_
        """
        return self.__base_delete(f'{self.url}/{product_id}',
                                  ['write_products'])

    def list(self, data):
        """List products.\n
        Scopes: 'write_products'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/products/products_list>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/products/products_list>`_
        """
        return self.__base_get(self.url, ['read_products'], data)

    @recharge_v1
    def count(self, data):
        """Count products.\n
        Scopes: 'write_products'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/products/products_count>`_
        """
        return self.__base_get(f'{self.url}/count', ['read_products'], data)
