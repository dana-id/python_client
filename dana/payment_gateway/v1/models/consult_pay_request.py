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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from dana.payment_gateway.v1.models.consult_pay_request_additional_info import ConsultPayRequestAdditionalInfo
from dana.payment_gateway.v1.models.consult_pay_request_amount import ConsultPayRequestAmount
from typing import Optional, Set
from typing_extensions import Self
from pydantic import AliasGenerator
from pydantic.alias_generators import to_camel

class ConsultPayRequest(BaseModel, BaseSdkModel):
    """
    ConsultPayRequest
    """ # noqa: E501
    merchant_id: Annotated[str, Field(strict=True, max_length=64)] = Field(description="Merchant identifier that is unique per each merchant")
    amount: ConsultPayRequestAmount
    additional_info: ConsultPayRequestAdditionalInfo = Field()
    __properties: ClassVar[List[str]] = ["merchantId", "amount", "additionalInfo"]

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
        """Create an instance of ConsultPayRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of additional_info
        if self.additional_info:
            _dict['additionalInfo'] = self.additional_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConsultPayRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "merchantId": obj.get("merchantId"),
            "amount": ConsultPayRequestAmount.from_dict(obj["amount"]) if obj.get("amount") is not None else None,
            "additionalInfo": ConsultPayRequestAdditionalInfo.from_dict(obj["additionalInfo"]) if obj.get("additionalInfo") is not None else None
        })
        return _obj


