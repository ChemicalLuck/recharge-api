from recharge.base import RechargeResource
from recharge.decorators import recharge_v1


class RechargeProduct(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/products
    """
    object_key = 'products'

    def create(self, data):
        """Create a product.
        https://developer.rechargepayments.com/2021-01/products/products_create
        """
        return self.__base_post(self.url, data)

    def retrieve(self, product_id):
        """Retrieve a product.
        https://developer.rechargepayments.com/2021-01/products/products_retrieve
        """
        return self.__base_get(f'{self.url}/{product_id}')

    def update(self, product_id, data):
        """Update a product.
        https://developer.rechargepayments.com/2021-01/products/products_update
        """
        return self.__base_put(f'{self.url}/{product_id}', data)

    def delete(self, product_id):
        """Delete a product.
        https://developer.rechargepayments.com/2021-01/products/products_delete
        """
        return self.__base_delete(f'{self.url}/{product_id}')

    def list(self, data):
        """List products.
        https://developer.rechargepayments.com/2021-01/products/products_list
        """
        return self.__base_get(self.url, data)

    @recharge_v1
    def count(self, data):
        """Count products.
        https://developer.rechargepayments.com/2021-01/products/products_count
        """
        return self.__base_get(f'{self.url}/count', data)
