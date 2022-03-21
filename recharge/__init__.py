import json
from requests import get

from recharge.constants import BASE_URL
from recharge.resources.addresses import RechargeAddress
from recharge.resources.charges import RechargeCharge
from recharge.resources.checkouts import RechargeCheckout
from recharge.resources.customers import RechargeCustomer
from recharge.resources.discounts import RechargeDiscount
from recharge.resources.metafields import RechargeMetafield
from recharge.resources.notifications import RechargeNotification
from recharge.resources.onetimes import RechargeOnetime
from recharge.resources.orders import RechargeOrder
from recharge.resources.paymentmethods import RechargePaymentMethod
from recharge.resources.plans import RechargePlan
from recharge.resources.products import RechargeProduct
from recharge.resources.subscriptions import RechargeSubscription
from recharge.resources.shops import RechargeShop
from recharge.resources.webhooks import RechargeWebhook


class Recharge(object):

    def __init__(self, api_key=None, version='2021-01', debug=False):
        self.api_key = api_key
        self.version = version
        self.debug = debug

        info = self._token_info(self.api_key)
        scopes = info[2]

        kwargs = {
            'api_key': api_key,
            'version': version,
            'debug': debug,
            'scopes': scopes,
        }

        self.Address = RechargeAddress(**kwargs)
        self.Charge = RechargeCharge(**kwargs)
        self.Checkout = RechargeCharge(**kwargs)
        self.Customer = RechargeCharge(**kwargs)
        self.Discount = RechargeCharge(**kwargs)
        self.Metafield = RechargeCharge(**kwargs)
        self.Notification = RechargeNotification(**kwargs)
        self.Onetime = RechargeCharge(**kwargs)
        self.Order = RechargeCharge(**kwargs)
        self.PaymentMethod = RechargePaymentMethod(**kwargs)
        self.Plan = RechargePlan(**kwargs)
        self.Product = RechargeCharge(**kwargs)
        self.Shop = RechargeShop(**kwargs)
        self.Subscription = RechargeCharge(**kwargs)
        self.Webhook = RechargeWebhook(**kwargs)

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