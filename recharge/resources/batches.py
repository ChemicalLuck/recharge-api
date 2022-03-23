from recharge.base import RechargeResource


class RechargeBatch(RechargeResource):
    """
    `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/async_batch_endpoints>`_\n
    `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/async_batch_endpoints>`_
    """
    object_key = 'async_batches'

    def create(self, data):
        """Crate an async batch.\n
        Scopes: 'write_batches'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/async_batch_endpoints/async_batch_endpoints_create>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/async_batch_endpoints/async_batch_endpoints_create>`_
        """
        self.__base_post(self.url, ['write_batches'], data)

    def retrieve(self, batch_id):
        """Retrieve a batch.\n
        Scopes: 'read_batches'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/async_batch_endpoints/async_batch_endpoints_retrieve>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/async_batch_endpoints/async_batch_endpoints_retrieve>`_
        """
        self.__base_get(f'{self.url}/{batch_id}', ['read_batches'])

    def list(self):
        """List batches.\n
        Scopes: 'read_batches'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/async_batch_endpoints/async_batch_endpoints_list>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/async_batch_endpoints/async_batch_endpoints_list>`_
        """
        self.__base_get(self.url, ['read_batches'])

    def process(self, batch_id):
        """Process a batch.\n
        Scopes: 'write_batches'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/async_batch_endpoints/async_batch_endpoints_process>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/async_batch_endpoints/async_batch_endpoints_process>`_
        """
        self.__base_post(f'{self.url}/{batch_id}/process', ['write_batches'],
                         {})

    def create_task(self, batch_id, data):
        """Create a batch task.\n
        Scopes: 'write_batches'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/async_batch_tasks/async_batch_tasks_create>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/async_batch_tasks/async_batch_tasks_create>`_
        """
        self.__base_post(f'{self.url}/{batch_id}/tasks', ['write_batches'],
                         data)

    def list_tasks(self, batch_id):
        """List batch tasks.\n
        Scopes: 'read_batches'\n
        `v1/2021-01 Docs <https://developer.rechargepayments.com/2021-01/async_batch_tasks/async_batch_tasks_retrieve>`_\n
        `v1/2021-11 Docs <https://developer.rechargepayments.com/2021-11/async_batch_tasks/async_batch_tasks_retrieve>`_
        """
        self.__base_get(f'{self.url}/{batch_id}/tasks', ['read_batches'], {})
