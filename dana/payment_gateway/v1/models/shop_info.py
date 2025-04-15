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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic import AliasGenerator
from pydantic.alias_generators import to_camel

class ShopInfo(BaseModel, BaseSdkModel):
    """
    ShopInfo
    """ # noqa: E501
    shop_id: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="Shop identifier (required if externalShopId is blank)")
    external_shop_id: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="External shop identifier (required if shopId is blank)")
    operator_id: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(default=None, description="Operator identifier")
    shop_address: Optional[Annotated[str, Field(strict=True, max_length=256)]] = Field(default=None, description="Shop address")
    division_id: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="Division identifier")
    external_division_id: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="External division identifier")
    division_type: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(default=None, description="Division type")
    shop_name: Optional[Annotated[str, Field(strict=True, max_length=128)]] = Field(default=None, description="Shop name")
    __properties: ClassVar[List[str]] = ["shopId", "externalShopId", "operatorId", "shopAddress", "divisionId", "externalDivisionId", "divisionType", "shopName"]

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
        """Create an instance of ShopInfo from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShopInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shopId": obj.get("shopId"),
            "externalShopId": obj.get("externalShopId"),
            "operatorId": obj.get("operatorId"),
            "shopAddress": obj.get("shopAddress"),
            "divisionId": obj.get("divisionId"),
            "externalDivisionId": obj.get("externalDivisionId"),
            "divisionType": obj.get("divisionType"),
            "shopName": obj.get("shopName")
        })
        return _obj


