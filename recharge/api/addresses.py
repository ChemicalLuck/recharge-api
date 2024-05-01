from typing import Required, TypedDict

from recharge.api import RechargeResource
from recharge.api.tokens import TokenScope


class AddressNoteAttributes(TypedDict):
    name: str
    value: str


class AddressShippingLinesOverride(TypedDict):
    code: str
    price: str
    title: str


class AddressCreateBody(TypedDict):
    address1: Required[str]
    address2: Required[str]
    cart_note: str
    city: Required[str]
    company: str
    country: Required[str]
    first_name: Required[str]
    last_name: Required[str]
    note_attributes: list[AddressNoteAttributes]
    phone: Required[str]
    presentment_currency: str
    province: Required[str]
    shipping_lines_override: list[AddressShippingLinesOverride]
    zip: Required[str]


class AddressUpdateBody(TypedDict):
    address1: str
    address2: str
    cart_note: str
    city: str
    company: str
    country: str
    first_name: str
    last_name: str
    note_attributes: list[AddressNoteAttributes]
    phone: str
    province: str
    shipping_lines_override: list[AddressShippingLinesOverride]
    zip: str


class AddressListQuery(TypedDict):
    created_at_max: str
    created_at_min: str
    customer_id: str
    discount_code: str
    discount_id: str
    ids: str
    limit: int
    page: int
    updated_at_max: str
    updated_at_min: str


class AddressCountQuery(TypedDict):
    created_at_max: str
    created_at_min: str
    discount_code: str
    discount_id: str
    updated_at_max: str
    updated_at_min: str


class AddressValidateBody(TypedDict):
    address1: str
    city: str
    state: str
    zipcode: str


class AddressApplyDiscountCode(TypedDict):
    discount_code: str


class AddressApplyDiscountId(TypedDict):
    discount_id: str


class AddressResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/addresses
    """

    object_list_key = "addresses"

    def create(self, customer_id, body: AddressCreateBody):
        """Create an address for the customer.
        https://developer.rechargepayments.com/2021-01/addresses/create_address
        """
        required_scopes: list[TokenScope] = ["write_customers"]
        self.check_scopes("POST /customers/:customer_id/addresses", required_scopes)

        url = f"{self.base_url}/customers/{customer_id}/{self.object_list_key}"
        return self.http_post(url, body)

    def get(self, address_id: str):
        """Get an address by ID.
        https://developer.rechargepayments.com/2021-01/addresses/retrieve_address
        """
        required_scopes: list[TokenScope] = ["read_customers"]
        self.check_scopes(f"GET {self.object_list_key}/:address_id", required_scopes)

        return self.http_get(f"{self.url}/{address_id}")

    def update(self, address_id, body: AddressUpdateBody | None = None):
        """Update an address by ID.
        https://developer.rechargepayments.com/2021-01/addresses/update_address
        """
        required_scopes: list[TokenScope] = ["write_customers"]
        self.check_scopes(f"PUT {self.object_list_key}/:id", required_scopes)

        return self.http_put(f"{self.url}/{address_id}", body)

    def delete(self, address_id):
        """Delete an address by ID.
        https://developer.rechargepayments.com/2021-01/addresses/delete_address
        """
        required_scopes: list[TokenScope] = ["write_customers"]
        self.check_scopes(f"DELETE {self.object_list_key}/:address_id", required_scopes)

        return self.http_delete(f"{self.url}/{address_id}")

    def list(self, customer_id, query: AddressListQuery | None = None):
        """List all addresses for a customer.
        https://developer.rechargepayments.com/2021-01/addresses/list_addresses
        """
        required_scopes: list[TokenScope] = ["read_customers"]
        self.check_scopes(
            f"GET /customers/:customer_id/{self.object_list_key}", required_scopes
        )

        return self.http_get(
            f"{self.base_url}/customers/{customer_id}/{self.object_list_key}", query
        )

    def count(self, query: AddressCountQuery | None = None):
        """Retrieve the count of addresses.
        https://developer.rechargepayments.com/2021-01/addresses/count_addresses
        """
        required_scopes: list[TokenScope] = ["read_customers"]
        self.check_scopes("GET /addresses/count", required_scopes)

        return self.http_get(f"{self.url}/count", query)

    def validate(self, body: AddressValidateBody):
        """Validate an address.
        https://developer.rechargepayments.com/2021-01/addresses/validate_address
        """

        return self.http_post(f"{self.url}/validate_address", body)

    def apply_discount(
        self,
        address_id,
        body: AddressApplyDiscountCode | AddressApplyDiscountId,
    ):
        """Apply a discount code to an address.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_apply_address
        """
        required_scopes: list[TokenScope] = ["write_discounts"]
        self.check_scopes("POST /addresses/:address_id/apply_discount", required_scopes)

        return self.http_post(f"{self.url}/{address_id}/apply_discount", body)

    def remove_discount(self, address_id: str):
        """Remove a discount from an address.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_remove_from_address_or_charge
        """
        required_scopes: list[TokenScope] = ["write_discounts"]
        self.check_scopes(
            "POST /addresses/:address_id/remove_discount", required_scopes
        )

        return self.http_post(f"{self.url}/{address_id}/remove_discount")
