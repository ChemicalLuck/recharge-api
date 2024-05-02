from typing import Literal, TypedDict, TypeAlias

from recharge.api import RechargeResource, RechargeScope

from .discounts import DiscountCreateBody, DiscountUpdateBody, DiscountDeleteBody
from .plans import (
    PlanCreateBody,
    PlanUpdateBody,
    PlanDeleteBody,
)
from .onetimes import OnetimeCreateBody, OnetimeDeleteBody


AsyncBatchType: TypeAlias = Literal[
    "discount_create",
    "discount_delete",
    "discount_update",
    "bulk_plans_create",
    "bulk_plans_update",
    "bulk_plans_delete",
    "onetime_create",
    "onetime_delete",
]


class AsyncBatchCreateBody(TypedDict):
    batch_type: AsyncBatchType


AsyncBatchBody: TypeAlias = (
    DiscountCreateBody
    | DiscountDeleteBody
    | DiscountUpdateBody
    | PlanCreateBody
    | PlanUpdateBody
    | PlanDeleteBody
    | OnetimeCreateBody
    | OnetimeDeleteBody
)


class AsyncBatchCreateTaskBody(TypedDict):
    body: AsyncBatchBody


class AsyncBatchResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/async_batch_endpoints
    """

    object_list_key = "async_batches"

    def create(self, body: AsyncBatchCreateBody):
        """Create an async batch.
        https://developer.rechargepayments.com/2021-11/async_batch_endpoints
        """
        required_scopes: list[RechargeScope] = ["write_batches"]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def create_task(self, batch_id, body: AsyncBatchCreateTaskBody):
        """Create a task for an async batch.
        https://developer.rechargepayments.com/2021-11/async_batch_endpoints
        """
        required_scopes: list[RechargeScope] = ["write_batches"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:batch_id/tasks", required_scopes
        )

        return self._http_post(f"{self.url}/{batch_id}/tasks", body)

    def get(self, batch_id):
        """Get an async batch.
        https://developer.rechargepayments.com/2021-11/async_batch_endpoints
        """
        required_scopes: list[RechargeScope] = ["read_batches"]
        self.check_scopes(f"GET /{self.object_list_key}/:batch_id", required_scopes)

        return self._http_get(f"{self.url}/{batch_id}")

    def list(self):
        """List async batches.
        https://developer.rechargepayments.com/2021-11/async_batch_endpoints
        """
        required_scopes: list[RechargeScope] = ["read_batches"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url)

    def list_tasks(
        self,
        batch_id,
    ):
        """List tasks for an async batch.
        https://developer.rechargepayments.com/2021-11/async_batch_endpoints
        """
        required_scopes: list[RechargeScope] = ["read_batches"]
        self.check_scopes(
            f"GET /{self.object_list_key}/:batch_id/tasks", required_scopes
        )

        return self._http_get(f"{self.url}/{batch_id}/tasks")

    def process(self, batch_id):
        """Process an async batch.
        https://developer.rechargepayments.com/2021-11/async_batch_endpoints
        """
        required_scopes: list[RechargeScope] = ["write_batches"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:batch_id/process", required_scopes
        )

        return self._http_post(f"{self.url}/{batch_id}/process", None)