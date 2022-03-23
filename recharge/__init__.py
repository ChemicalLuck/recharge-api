import json

from requests import get

from recharge.constants import ALLOWED_VERSIONS, BASE_URL
from recharge.exceptions import AuthenticationError
from recharge.resources.accounts import RechargeAccount
from recharge.resources.addresses import RechargeAddress
from recharge.resources.batches import RechargeBatch
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
from recharge.resources.shops import RechargeShop, RechargeStore
from recharge.resources.subscriptions import RechargeSubscription
from recharge.resources.webhooks import RechargeWebhook


class Recharge(object):

    def __init__(self, api_key=None, version='2021-01', validate_scopes=False,
                 debug=False):
        """
        A wrapper for the 'requests' library to make interacting with the
        `Recharge API <https://support.rechargepayments.com/hc/en-us/articles/360008829993-Recharge-API->`_,
        really straight-forward.\n
        It can utilise both versions, v1/2021-01 and
        v2/2021-11 however some methods are only available to specific versions.
        Please note that identical methods between versions may have different
        schema with regard to query parameters.\n
        When you try to use a 'version-locked' method, headers will
        automatically change the client version to match the method and then
        revert upon completion
        :param str api_key: Create/Find in the 'Apps' tab of the Recharge Admin
        :param str version: Which API version to use
        :param bool validate_scopes: Check scopes before request. May decrease speed
        :param bool debug: See more info about the request URL and rate limits
        """

        self.api_key = api_key
        self.debug = debug
        self.validate_scopes = validate_scopes

        if version in ALLOWED_VERSIONS:
            self.version = version
        else:
            raise ValueError(
                    f"{version} not in allowed versions: {ALLOWED_VERSIONS}")

        info = self.__token_info(self.api_key)
        scopes = info[2]
        self.scopes = info[2]

        kwargs = {
            'api_key': api_key,
            'version': version,
            'validate_scopes': validate_scopes,
            'debug': debug,
            'scopes': scopes,
        }

        self.Account = RechargeAccount(**kwargs)
        self.Address = RechargeAddress(**kwargs)
        self.Batch = RechargeBatch(**kwargs)
        self.Charge = RechargeCharge(**kwargs)
        self.Checkout = RechargeCheckout(**kwargs)
        self.Customer = RechargeCustomer(**kwargs)
        self.Discount = RechargeDiscount(**kwargs)
        self.Metafield = RechargeMetafield(**kwargs)
        self.Notification = RechargeNotification(**kwargs)
        self.Onetime = RechargeOnetime(**kwargs)
        self.Order = RechargeOrder(**kwargs)
        self.PaymentMethod = RechargePaymentMethod(**kwargs)
        self.Plan = RechargePlan(**kwargs)
        self.Product = RechargeProduct(**kwargs)
        self.Shop = RechargeShop(**kwargs)
        self.Store = RechargeStore(**kwargs)
        self.Subscription = RechargeSubscription(**kwargs)
        self.Webhook = RechargeWebhook(**kwargs)

    @staticmethod
    def __token_info(api_key) -> tuple[str, str, list[str]]:
        headers = {
            'Accept':                  'application/json',
            'Content-Type':            'application/json',
            'X-Recharge-Access-Token': api_key,
        }
        url = BASE_URL + "/token_information"
        response = get(url, headers=headers)
        if response.status_code == 401:
            raise AuthenticationError(f"Status code {response.status_code}. API Key invalid, please check Recharge.")
        data = json.loads(response.text)
        return data["name"], data["contact_email"], data["scopes"]
