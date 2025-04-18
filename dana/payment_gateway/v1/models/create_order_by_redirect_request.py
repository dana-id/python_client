# Copyright 2025 PT Espay Debit Indonesia Koe
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Payment Gateway API

    API for doing operations in DANA Payment Gateway (Gapura)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from dana.base.model import BaseSdkModel

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dana.payment_gateway.v1.models.create_order_by_redirect_additional_info import CreateOrderByRedirectAdditionalInfo
from dana.payment_gateway.v1.models.money import Money
from dana.payment_gateway.v1.models.url_param import UrlParam
from typing import Optional, Set
from typing_extensions import Self
from pydantic import AliasGenerator
from pydantic.alias_generators import to_camel

class CreateOrderByRedirectRequest(BaseModel, BaseSdkModel):
    """
    CreateOrderByRedirectRequest
    """ # noqa: E501
    additional_info: Optional[CreateOrderByRedirectAdditionalInfo] = Field(default=None)
    partner_reference_no: Annotated[str, Field(strict=True, max_length=64)] = Field(description="Transaction identifier on partner system")
    merchant_id: Annotated[str, Field(strict=True, max_length=64)] = Field(description="Unique merchant identifier")
    amount: Money
    sub_merchant_id: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(default=None, description="Information of sub merchant identifier")
    external_store_id: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="Store identifier to indicate to which store this payment belongs to")
    valid_up_to: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The date and time when the order is valid until in the following format: YYYY-MM-DDTHH:MM:SS+07:00 ")
    disabled_pay_methods: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="Payment method(s) that cannot be used for this")
    url_params: List[UrlParam] = Field(description="Notify URL that DANA must send the payment notification to")
    __properties: ClassVar[List[str]] = ["partnerReferenceNo", "merchantId", "amount", "subMerchantId", "externalStoreId", "validUpTo", "disabledPayMethods", "urlParams"]

    @field_validator('valid_up_to')
    def valid_up_to_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+07:00$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+07:00$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        alias_generator=AliasGenerator(serialization_alias=to_camel, validation_alias=to_camel),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict(), separators=(',', ':'))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateOrderByRedirectRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in url_params (list)
        _items = []
        if self.url_params:
            for _item_url_params in self.url_params:
                if _item_url_params:
                    _items.append(_item_url_params.to_dict())
            _dict['urlParams'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOrderByRedirectRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "partnerReferenceNo": obj.get("partnerReferenceNo"),
            "merchantId": obj.get("merchantId"),
            "amount": Money.from_dict(obj["amount"]) if obj.get("amount") is not None else None,
            "subMerchantId": obj.get("subMerchantId"),
            "externalStoreId": obj.get("externalStoreId"),
            "validUpTo": obj.get("validUpTo"),
            "disabledPayMethods": obj.get("disabledPayMethods"),
            "urlParams": [UrlParam.from_dict(_item) for _item in obj["urlParams"]] if obj.get("urlParams") is not None else None
        })
        return _obj


