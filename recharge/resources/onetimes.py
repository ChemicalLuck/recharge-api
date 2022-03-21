from recharge.base import RechargeResource


class RechargeOnetime(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/onetimes
    """
    object_key = 'onetimes'

    def create(self, data):
        """Create a onetime.
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_create
        """
        return self.__base_post(self.url, data)

    def retrieve(self, onetime_id):
        """Retrieve a onetime.
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_retrieve
        """
        return self.__base_get(f'{self.url}/{onetime_id}')

    def update(self, onetime_id, data):
        """Update a onetime.
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_update
        """
        return self.__base_put(f'{self.url}/{onetime_id}', data)

    def delete(self, onetime_id):
        """Delete a onetime.
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_delete
        """
        return self.__base_delete(f'{self.url}/{onetime_id}')

    def list(self, data=None):
        """List onetimes.
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_list
        """
        return self.__base_get(self.url, data)