from recharge.api.tokens import TokenScope
from recharge.api import RechargeResource

from typing import TypedDict, Required, Literal

type ProductDiscountType = Literal["percentage"]

type ProductStorefrontPurchaseOptions = Literal[
    "subscription_only", "subscription_and_onetime"
]


class ProductCreateBody(TypedDict):
    charge_interval_frequency: int
    cutoff_day_of_month: int
    cutoff_day_of_week: int
    discount_amount: str
    discount_type: ProductDiscountType
    expire_after_specific_number_of_charges: str
    modifiable_properties: list[str]
    order_day_of_month: int
    order_day_of_week: int
    order_interval_frequency_options: list[int]
    shopify_product_id: Required[int]
    storefront_purchase_options: ProductStorefrontPurchaseOptions


class ProductImages(TypedDict):
    large: str
    medium: str
    original: str
    small: str


type ProductOrderIntervalUnit = Literal["day", "week", "month"]


class ProductGetQuery(TypedDict):
    charge_interval_frequency: str
    created_at: str
    cutoff_day_of_month: str
    cutoff_day_of_week: str
    discount_amount: str
    discount_type: ProductDiscountType
    expire_after_specific_number_of_charges: str
    handle: str
    images: ProductImages
    modifiable_properties: list[str]
    number_charges_until_expiration: str
    order_day_of_month: str
    order_day_of_week: str
    order_interval_frequency: str
    order_interval_unit: ProductOrderIntervalUnit
    shopify_product_id: str
    storefront_purchase_options: ProductStorefrontPurchaseOptions
    title: str
    updated_at: str


class ProductUpdateBody(TypedDict):
    charge_interval_frequency: int
    cutoff_day_of_month: int
    cutoff_day_of_week: int
    discount_amount: str
    discount_type: ProductDiscountType
    expire_after_specific_number_of_charges: str
    modifiable_properties: list[str]
    order_day_of_month: int
    order_day_of_week: int
    order_interval_unit: ProductOrderIntervalUnit
    shopify_product_id: Required[int]
    storefront_purchase_options: ProductStorefrontPurchaseOptions


class ProductListQuery(TypedDict):
    id: str
    limit: str
    shopify_product_id: int
    page: str


class ProductResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/products
    """

    object_list_key = "products"

    def create(self, body: ProductCreateBody):
        """Create a product.
        https://developer.rechargepayments.com/2021-01/products/products_create
        """
        required_scopes: list[TokenScope] = ["write_products"]
        self.check_scopes("POST /products", required_scopes)

        return self.http_post(self.url, body)

    def get(self, product_id: str):
        """Get a product.
        https://developer.rechargepayments.com/2021-01/products/products_retrieve
        """
        required_scopes: list[TokenScope] = ["read_products"]
        self.check_scopes(f"GET /products/{product_id}", required_scopes)

        return self.http_get(f"{self.url}/{product_id}")

    def update(self, product_id: str, body: ProductUpdateBody):
        """Update a product.
        https://developer.rechargepayments.com/2021-01/products/products_update
        """
        required_scopes: list[TokenScope] = ["write_products"]
        self.check_scopes(f"PUT /products/{product_id}", required_scopes)

        return self.http_put(f"{self.url}/{product_id}", body)

    def delete(self, product_id: str):
        """Delete a product.
        https://developer.rechargepayments.com/2021-01/products/products_delete
        """
        required_scopes: list[TokenScope] = ["write_products"]
        self.check_scopes(f"DELETE /products/{product_id}", required_scopes)

        return self.http_delete(f"{self.url}/{product_id}")

    def list(self, query: ProductListQuery):
        """List products.
        https://developer.rechargepayments.com/2021-01/products/products_list
        """
        required_scopes: list[TokenScope] = ["read_products"]
        self.check_scopes("GET /products", required_scopes)

        return self.http_get(self.url, query)

    def count(self):
        """Count products.
        https://developer.rechargepayments.com/2021-01/products/products_count
        """
        required_scopes: list[TokenScope] = ["read_products"]
        self.check_scopes("GET /products/count", required_scopes)

        return self.http_get(f"{self.url}/count")
