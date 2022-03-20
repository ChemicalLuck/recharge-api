import json
from requests import get

from recharge.constants import BASE_URL
from recharge.resources.addresses import RechargeAddress
from recharge.resources.charges import RechargeCharge
from recharge.resources.checkouts import RechargeCheckout
from recharge.resources.customers import RechargeCustomer
from recharge.resources.discounts import RechargeDiscount
from recharge.resources.metafields import RechargeMetafield
from recharge.resources.onetimes import RechargeOnetime
from recharge.resources.orders import RechargeOrder
from recharge.resources.products import RechargeProduct
from recharge.resources.subscriptions import RechargeSubscription
from recharge.resources.webhooks import RechargeWebhook
from recharge.resources.shops import RechargeShop


class Recharge(object):

    def __init__(self, api_key=None, debug=False):
        self.api_key = api_key
        self.debug = debug

        info = self._token_info(self.api_key)
        scopes = info[2]

        kwargs = {
            'api_key': api_key,
            'debug': debug,
            'scopes': scopes,
        }

        self.Address = RechargeAddress(**kwargs)
        self.Charge = RechargeCharge(**kwargs)
        self.Checkout = RechargeCharge(**kwargs)
        self.Customer = RechargeCharge(**kwargs)
        self.Order = RechargeCharge(**kwargs)
        self.Subscription = RechargeCharge(**kwargs)
        self.Onetime = RechargeCharge(**kwargs)
        self.Discount = RechargeCharge(**kwargs)
        self.Webhook = RechargeWebhook(**kwargs)
        self.Metafield = RechargeCharge(**kwargs)
        self.Shop = RechargeShop(**kwargs)
        self.Product = RechargeCharge(**kwargs)

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