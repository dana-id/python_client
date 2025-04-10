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
from dana.payment_gateway.v1.models.money import Money
from dana.payment_gateway.v1.models.query_payment_response_additional_info import QueryPaymentResponseAdditionalInfo
from typing import Optional, Set
from typing_extensions import Self
from pydantic import AliasGenerator
from pydantic.alias_generators import to_camel

class QueryPaymentResponse(BaseModel, BaseSdkModel):
    """
    QueryPaymentResponse
    """ # noqa: E501
    response_code: Annotated[str, Field(strict=True, max_length=7)] = Field(description="Refer to response code list:<br> * 2005500 - Successful<br> * 4005500 - Bad Request - Retry request with proper parameter<br> * 4005501 - Invalid Field Format - Retry request with proper parameter<br> * 4005502 - Invalid Mandatory Field - Retry request with proper parameter<br> * 4015500 - Unauthorized. [reason] - Retry request with proper parameter<br> * 4015501 - Invalid Token (B2B) - Retry request with proper parameter<br> * 4045501 - Transaction Not Found - Try to create a new order<br> * 4295500 - Too Many Requests - Retry request periodically<br> * 5005500 - General Error - Retry request periodically<br> * 5005501 - Internal Server Error - Retry request periodically<br> ")
    response_message: Annotated[str, Field(strict=True, max_length=150)] = Field(description="Refer to response code list ")
    original_partner_reference_no: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="Original transaction identifier on partner system")
    original_reference_no: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="Original transaction identifier on DANA system")
    original_external_id: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(default=None, description="Original external identifier on header message")
    service_code: Annotated[str, Field(strict=True, max_length=2)] = Field(description="Transaction type indicator:<br> - IPG Cashier Pay - SNAP: 54<br> - QRIS CPM (Acquirer) - SNAP: 60<br> - QRIS MPM (Acquirer) - SNAP: 47<br> - Payment Gateway: 54<br> ")
    latest_transaction_status: Annotated[str, Field(strict=True, max_length=2)] = Field(description="Status code:<br> - 00 = Success. Order has been successfully in final state and paid<br> - 01 = Initiated. Waiting for payment. Mark Payment as Pending<br> - 02 = Paying. The order is in process, not in final state, payment is success. Mark Payment as Success<br> - 05 = Cancelled. Order has been cancelled. Mark Payment as Failed<br> - 07 = Not found. Order is not found. Mark Payment as Failed<br> ")
    transaction_status_desc: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="Description of transaction status")
    original_response_code: Optional[Annotated[str, Field(strict=True, max_length=7)]] = Field(default=None, description="Original response code")
    original_response_message: Optional[Annotated[str, Field(strict=True, max_length=150)]] = Field(default=None, description="Original response message")
    session_id: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Session identifier")
    request_id: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Transaction request identifier")
    trans_amount: Optional[Money] = Field(default=None)
    amount: Optional[Money] = None
    fee_amount: Optional[Money] = Field(default=None)
    paid_time: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Payment timestamp in format YYYY-MM-DDTHH:mm:ss+07:00 (Jakarta time)")
    title: Optional[Annotated[str, Field(strict=True, max_length=256)]] = Field(default=None, description="Brief description of transaction")
    additional_info: Optional[QueryPaymentResponseAdditionalInfo] = Field(default=None)
    __properties: ClassVar[List[str]] = ["responseCode", "responseMessage", "originalPartnerReferenceNo", "originalReferenceNo", "originalExternalId", "serviceCode", "latestTransactionStatus", "transactionStatusDesc", "originalResponseCode", "originalResponseMessage", "sessionId", "requestID", "transAmount", "amount", "feeAmount", "paidTime", "title", "additionalInfo"]

    @field_validator('paid_time')
    def paid_time_validate_regular_expression(cls, value):
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
        return json.dumps(self.to_dict(), separators=(',', ': '))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of QueryPaymentResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of trans_amount
        if self.trans_amount:
            _dict['transAmount'] = self.trans_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fee_amount
        if self.fee_amount:
            _dict['feeAmount'] = self.fee_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of additional_info
        if self.additional_info:
            _dict['additionalInfo'] = self.additional_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QueryPaymentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "responseCode": obj.get("responseCode"),
            "responseMessage": obj.get("responseMessage"),
            "originalPartnerReferenceNo": obj.get("originalPartnerReferenceNo"),
            "originalReferenceNo": obj.get("originalReferenceNo"),
            "originalExternalId": obj.get("originalExternalId"),
            "serviceCode": obj.get("serviceCode") if obj.get("serviceCode") is not None else '54',
            "latestTransactionStatus": obj.get("latestTransactionStatus"),
            "transactionStatusDesc": obj.get("transactionStatusDesc"),
            "originalResponseCode": obj.get("originalResponseCode"),
            "originalResponseMessage": obj.get("originalResponseMessage"),
            "sessionId": obj.get("sessionId"),
            "requestID": obj.get("requestID"),
            "transAmount": Money.from_dict(obj["transAmount"]) if obj.get("transAmount") is not None else None,
            "amount": Money.from_dict(obj["amount"]) if obj.get("amount") is not None else None,
            "feeAmount": Money.from_dict(obj["feeAmount"]) if obj.get("feeAmount") is not None else None,
            "paidTime": obj.get("paidTime"),
            "title": obj.get("title"),
            "additionalInfo": QueryPaymentResponseAdditionalInfo.from_dict(obj["additionalInfo"]) if obj.get("additionalInfo") is not None else None
        })
        return _obj


