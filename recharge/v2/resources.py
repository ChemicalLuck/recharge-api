from recharge.base import BaseResource


class V2BaseResource(BaseResource):

    def __init__(self):
        super().__init__()
        self.headers['X-Recharge-Version'] = '2021-11'


class V2AddressResource(V2BaseResource):
    object_key = 'addresses'


class V2ChargeResource(V2BaseResource):
    object_key = 'charges'


class V2CheckoutResource(V2BaseResource):
    object_key = 'checkouts'


class V2CustomerResource(V2BaseResource):
    object_key = 'customers'


class V2OrderResource(V2BaseResource):
    object_key = 'orders'


class V2SubscriptionResource(V2BaseResource):
    object_key = 'subscriptions'


class V2OnetimeResource(V2BaseResource):
    object_key = 'onetimes'


class V2DiscountResource(V2BaseResource):
    object_key = 'discounts'


class V2WebhookResource(V2BaseResource):
    object_key = 'webhooks'


class V2MetafieldResource(V2BaseResource):
    object_key = 'metafields'


class V2ShopResource(V2BaseResource):
    object_key = 'shop'


class V2ProductResource(V2BaseResource):
    object_key = 'products'