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
from dana.payment_gateway.v1.models.create_order_response_additional_info import CreateOrderResponseAdditionalInfo
from typing import Optional, Set
from typing_extensions import Self
from pydantic import AliasGenerator
from pydantic.alias_generators import to_camel

class CreateOrderResponse(BaseModel, BaseSdkModel):
    """
    CreateOrderResponse
    """ # noqa: E501
    response_code: Annotated[str, Field(strict=True, max_length=7)] = Field(description="Response code for the transaction result. Example values include:<br> * 2005400 - Successful<br> * 4005400 - Bad Request - Retry request with proper parameter<br> * 4005401 - Invalid Field Format - Retry request with proper parameter<br> * 4005402 - Invalid Mandatory Field - Retry request with proper parameter<br> * 4015400 - Unauthorized. Invalid Signature - Retry request with proper parameter<br> * 4035402 - Exceeds Transaction Amount Limit - Try to adjust the order amount<br> * 4035405 - Do Not Honor - Retry request with proper parameter or can contact DANA to check the user/account status<br> * 4035415 - Transaction Not Permitted - Retry request periodically or consult to DANA<br> * 4045408 - Invalid Merchant - Retry request with proper parameter<br> * 4045418 - Inconsistent Request - Retry with proper parameter<br> * 4295400 - Too Many Requests - Retry request periodically by sending same request payload<br> * 5005400 - General Error - Retry request periodically<br> * 5005401 - Internal Server Error - Retry request periodically by sending same request payload<br> ")
    response_message: Annotated[str, Field(strict=True, max_length=150)] = Field(description="Message corresponding to the response code")
    reference_no: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="Transaction identifier on DANA system (present if successfully processed)")
    partner_reference_no: Annotated[str, Field(strict=True, max_length=64)] = Field(description="Transaction identifier on partner system")
    web_redirect_url: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = Field(default=None, description="Checkout URL (present if payment method is not OVO/Virtual Account/QRIS)")
    additional_info: Optional[CreateOrderResponseAdditionalInfo] = Field(default=None)
    __properties: ClassVar[List[str]] = ["responseCode", "responseMessage", "referenceNo", "partnerReferenceNo", "webRedirectUrl", "additionalInfo"]

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
        """Create an instance of CreateOrderResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of additional_info
        if self.additional_info:
            _dict['additionalInfo'] = self.additional_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOrderResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "responseCode": obj.get("responseCode"),
            "responseMessage": obj.get("responseMessage"),
            "referenceNo": obj.get("referenceNo"),
            "partnerReferenceNo": obj.get("partnerReferenceNo"),
            "webRedirectUrl": obj.get("webRedirectUrl"),
            "additionalInfo": CreateOrderResponseAdditionalInfo.from_dict(obj["additionalInfo"]) if obj.get("additionalInfo") is not None else None
        })
        return _obj


