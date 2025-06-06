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
from dana.payment_gateway.v1.models.promo_info import PromoInfo
from typing import Optional, Set
from typing_extensions import Self
from pydantic import AliasGenerator
from pydantic.alias_generators import to_camel

class PaymentInfo(BaseModel, BaseSdkModel):
    """
    PaymentInfo
    """ # noqa: E501
    pay_method: Annotated[str, Field(strict=True, max_length=64)] = Field()
    pay_option: Optional[Annotated[str, Field(strict=True, max_length=128)]] = Field(default=None)
    promo_infos: Optional[List[PromoInfo]] = Field(default=None)
    __properties: ClassVar[List[str]] = ["payMethod", "payOption", "promoInfos"]

    @field_validator('pay_method')
    def pay_method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['BALANCE', 'COUPON', 'NET_BANKING', 'CREDIT_CARD', 'DEBIT_CARD', 'VIRTUAL_ACCOUNT', 'OTC', 'DIRECT_DEBIT_CREDIT_CARD', 'DIRECT_DEBIT_DEBIT_CARD', 'ONLINE_CREDIT', 'LOAN_CREDIT', 'NETWORK_PAY']):
            raise ValueError("must be one of enum values ('BALANCE', 'COUPON', 'NET_BANKING', 'CREDIT_CARD', 'DEBIT_CARD', 'VIRTUAL_ACCOUNT', 'OTC', 'DIRECT_DEBIT_CREDIT_CARD', 'DIRECT_DEBIT_DEBIT_CARD', 'ONLINE_CREDIT', 'LOAN_CREDIT', 'NETWORK_PAY')")
        return value

    @field_validator('pay_option')
    def pay_option_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NETWORK_PAY_PG_SPAY', 'NETWORK_PAY_PG_OVO', 'NETWORK_PAY_PG_GOPAY', 'NETWORK_PAY_PG_LINKAJA', 'NETWORK_PAY_PG_CARD', 'VIRTUAL_ACCOUNT_BCA', 'VIRTUAL_ACCOUNT_BNI', 'VIRTUAL_ACCOUNT_MANDIRI', 'VIRTUAL_ACCOUNT_BRI', 'VIRTUAL_ACCOUNT_BTPN', 'VIRTUAL_ACCOUNT_CIMB', 'VIRTUAL_ACCOUNT_PERMATA']):
            raise ValueError("must be one of enum values ('NETWORK_PAY_PG_SPAY', 'NETWORK_PAY_PG_OVO', 'NETWORK_PAY_PG_GOPAY', 'NETWORK_PAY_PG_LINKAJA', 'NETWORK_PAY_PG_CARD', 'VIRTUAL_ACCOUNT_BCA', 'VIRTUAL_ACCOUNT_BNI', 'VIRTUAL_ACCOUNT_MANDIRI', 'VIRTUAL_ACCOUNT_BRI', 'VIRTUAL_ACCOUNT_BTPN', 'VIRTUAL_ACCOUNT_CIMB', 'VIRTUAL_ACCOUNT_PERMATA')")
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
        """Create an instance of PaymentInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in promo_infos (list)
        _items = []
        if self.promo_infos:
            for _item_promo_infos in self.promo_infos:
                if _item_promo_infos:
                    _items.append(_item_promo_infos.to_dict())
            _dict['promoInfos'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "payMethod": obj.get("payMethod"),
            "payOption": obj.get("payOption"),
            "promoInfos": [PromoInfo.from_dict(_item) for _item in obj["promoInfos"]] if obj.get("promoInfos") is not None else None
        })
        return _obj


