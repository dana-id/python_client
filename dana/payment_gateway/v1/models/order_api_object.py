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
from dana.payment_gateway.v1.models.buyer import Buyer
from dana.payment_gateway.v1.models.goods import Goods
from dana.payment_gateway.v1.models.shipping_info import ShippingInfo
from typing import Optional, Set
from typing_extensions import Self
from pydantic import AliasGenerator
from pydantic.alias_generators import to_camel

class OrderApiObject(BaseModel, BaseSdkModel):
    """
    OrderApiObject
    """ # noqa: E501
    order_title: Annotated[str, Field(strict=True, max_length=64)] = Field()
    merchant_trans_type: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None)
    buyer: Buyer
    goods: Optional[List[Goods]] = None
    shipping_info: Optional[List[ShippingInfo]] = Field(default=None)
    extend_info: Optional[Annotated[str, Field(strict=True, max_length=4096)]] = Field(default=None)
    scenario: Optional[Annotated[str, Field(strict=True, max_length=64)]] = None
    __properties: ClassVar[List[str]] = ["orderTitle", "merchantTransType", "buyer", "goods", "shippingInfo", "extendInfo", "scenario"]

    @field_validator('scenario')
    def scenario_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['API']):
            raise ValueError("must be one of enum values ('API')")
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
        return json.dumps(self.to_dict(), separators=(',', ': '))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OrderApiObject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of buyer
        if self.buyer:
            _dict['buyer'] = self.buyer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in goods (list)
        _items = []
        if self.goods:
            for _item_goods in self.goods:
                if _item_goods:
                    _items.append(_item_goods.to_dict())
            _dict['goods'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in shipping_info (list)
        _items = []
        if self.shipping_info:
            for _item_shipping_info in self.shipping_info:
                if _item_shipping_info:
                    _items.append(_item_shipping_info.to_dict())
            _dict['shippingInfo'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderApiObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "orderTitle": obj.get("orderTitle"),
            "merchantTransType": obj.get("merchantTransType"),
            "buyer": Buyer.from_dict(obj["buyer"]) if obj.get("buyer") is not None else None,
            "goods": [Goods.from_dict(_item) for _item in obj["goods"]] if obj.get("goods") is not None else None,
            "shippingInfo": [ShippingInfo.from_dict(_item) for _item in obj["shippingInfo"]] if obj.get("shippingInfo") is not None else None,
            "extendInfo": obj.get("extendInfo"),
            "scenario": obj.get("scenario")
        })
        return _obj


