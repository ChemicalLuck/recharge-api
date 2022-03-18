from recharge.base import BaseResource


class V1BaseResource(BaseResource):

    def __init__(self):
        super().__init__()
        self.headers['X-Recharge-Version'] = '2021-01'


class V1AddressResource(V1BaseResource):
    object_key = 'addresses'


class V1ChargeResource(V1BaseResource):
    object_key = 'charges'


class V1CheckoutResource(V1BaseResource):
    object_key = 'checkouts'


class V1CustomerResource(V1BaseResource):
    object_key = 'customers'


class V1OrderResource(V1BaseResource):
    object_key = 'orders'


class V1SubscriptionResource(V1BaseResource):
    object_key = 'subscriptions'


class V1OnetimeResource(V1BaseResource):
    object_key = 'onetimes'


class V1DiscountResource(V1BaseResource):
    object_key = 'discounts'


class V1WebhookResource(V1BaseResource):
    object_key = 'webhooks'


class V1MetafieldResource(V1BaseResource):
    object_key = 'metafields'


class V1ShopResource(V1BaseResource):
    object_key = 'shop'


class V1ProductResource(V1BaseResource):
    object_key = 'products'