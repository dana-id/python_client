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
from dana.payment_gateway.v1.models.money import Money
from typing import Optional, Set
from typing_extensions import Self
from pydantic import AliasGenerator
from pydantic.alias_generators import to_camel

class ShippingInfo(BaseModel, BaseSdkModel):
    """
    ShippingInfo
    """ # noqa: E501
    merchant_shipping_id: Annotated[str, Field(strict=True, max_length=64)] = Field(description="Merchant shipping identifier")
    tracking_no: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="Number of tracking")
    carrier: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="Information of carrier")
    charge_amount: Optional[Money] = Field(default=None, description="Promo amount. Contains two sub-fields:<br> 1. Value: Transaction amount, including the cents<br> 2. Currency: Currency code based on ISO<br> ")
    country_name: Annotated[str, Field(strict=True, max_length=64)] = Field(description="Name of country")
    state_name: Annotated[str, Field(strict=True, max_length=64)] = Field(description="Name of state")
    city_name: Annotated[str, Field(strict=True, max_length=64)] = Field(description="Name of city")
    area_name: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="Name of area")
    address1: Annotated[str, Field(strict=True, max_length=256)] = Field(description="Information of address 1")
    address2: Optional[Annotated[str, Field(strict=True, max_length=256)]] = Field(default=None, description="Information of address 2")
    first_name: Annotated[str, Field(strict=True, max_length=64)] = Field(description="First name")
    last_name: Annotated[str, Field(strict=True, max_length=64)] = Field(description="Last name")
    mobile_no: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(default=None, description="Mobile number")
    phone_no: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(default=None, description="Phone number")
    zip_code: Annotated[str, Field(strict=True, max_length=32)] = Field(description="Zip code")
    email: Optional[Annotated[str, Field(strict=True, max_length=128)]] = Field(default=None, description="Email")
    fax_no: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(default=None, description="Fax number")
    __properties: ClassVar[List[str]] = ["merchantShippingId", "trackingNo", "carrier", "chargeAmount", "countryName", "stateName", "cityName", "areaName", "address1", "address2", "firstName", "lastName", "mobileNo", "phoneNo", "zipCode", "email", "faxNo"]

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
        """Create an instance of ShippingInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of charge_amount
        if self.charge_amount:
            _dict['chargeAmount'] = self.charge_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShippingInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "merchantShippingId": obj.get("merchantShippingId"),
            "trackingNo": obj.get("trackingNo"),
            "carrier": obj.get("carrier"),
            "chargeAmount": Money.from_dict(obj["chargeAmount"]) if obj.get("chargeAmount") is not None else None,
            "countryName": obj.get("countryName"),
            "stateName": obj.get("stateName"),
            "cityName": obj.get("cityName"),
            "areaName": obj.get("areaName"),
            "address1": obj.get("address1"),
            "address2": obj.get("address2"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "mobileNo": obj.get("mobileNo"),
            "phoneNo": obj.get("phoneNo"),
            "zipCode": obj.get("zipCode"),
            "email": obj.get("email"),
            "faxNo": obj.get("faxNo")
        })
        return _obj


