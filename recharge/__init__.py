import json
from requests import get

from recharge.constants import BASE_URL
from recharge.v1.resources import (
    V1AddressResource,
    V1ChargeResource,
    V1CheckoutResource,
    V1CustomerResource,
    V1OrderResource,
    V1SubscriptionResource,
    V1OnetimeResource,
    V1DiscountResource,
    V1WebhookResource,
    V1MetafieldResource,
    V1ShopResource,
    V1ProductResource
)
from recharge.v2.resources import (
    V2AddressResource,
    V2ChargeResource,
    V2CheckoutResource,
    V2CustomerResource,
    V2OrderResource,
    V2SubscriptionResource,
    V2OnetimeResource,
    V2DiscountResource,
    V2WebhookResource,
    V2MetafieldResource,
    V2ShopResource,
    V2ProductResource
)


class Recharge(object):

    def __init__(self, api_key=None, version='2021-01', debug=False):
        self.api_key = api_key
        self.version = version
        self.debug = debug

        info = self._token_info(self.api_key)
        scopes = info[2]

        kwargs = {
            'api_key': api_key,
            'debug': debug,
            'scopes': scopes,
        }

        if self.version == '2021-01':
            self.Address = V1AddressResource(**kwargs)
            self.Charge = V1ChargeResource(**kwargs)
            self.Checkout = V1CheckoutResource(**kwargs)
            self.Customer = V1CustomerResource(**kwargs)
            self.Order = V1OrderResource(**kwargs)
            self.Subscription = V1SubscriptionResource(**kwargs)
            self.Onetime = V1OnetimeResource(**kwargs)
            self.Discount = V1DiscountResource(**kwargs)
            self.Webhook = V1WebhookResource(**kwargs)
            self.Metafield = V1MetafieldResource(**kwargs)
            self.Shop = V1ShopResource(**kwargs)
            self.Product = V1ProductResource(**kwargs)
        elif self.version == '2021-11':
            self.Address = V1AddressResource(**kwargs)
            self.Charge = V2ChargeResource(**kwargs)
            self.Checkout = V2CheckoutResource(**kwargs)
            self.Customer = V2CustomerResource(**kwargs)
            self.Order = V2OrderResource(**kwargs)
            self.Subscription = V2SubscriptionResource(**kwargs)
            self.Onetime = V2OnetimeResource(**kwargs)
            self.Discount = V2DiscountResource(**kwargs)
            self.Webhook = V2WebhookResource(**kwargs)
            self.Metafield = V2MetafieldResource(**kwargs)
            self.Shop = V2ShopResource(**kwargs)
            self.Product = V2ProductResource(**kwargs)
        else:
            assert self.version in ['2021-01', '2021-11']

    @staticmethod
    def _token_info(api_key) -> tuple[str, str, list[str]]:
        headers = {
            'Accept':                  'application/json',
            'Content-Type':            'application/json',
            'X-Recharge-Access-Token': api_key,
        }
        url = BASE_URL + "/token_information"
        response = get(url, headers=headers)
        data = json.loads(response.text)
        return data["name"], data["contact_email"], data["scopes"]


if __name__ == '__main__':
    Recharge("23d3021138230cbb00843c249a5e5109d67586d222c80fc7e9780551")