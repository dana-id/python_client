# CancelOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Response code. Refer to https://dashboard.dana.id/api-docs/read/117#HTML-API-CancelOrder-ResponseCodeandMessage | 
**response_message** | **str** | Response message. Refer to https://dashboard.dana.id/api-docs/read/117#HTML-API-CancelOrder-ResponseCodeandMessage | 
**original_reference_no** | **str** | Original transaction identifier on DANA system. Present if successfully processed | [optional] 
**original_partner_reference_no** | **str** | Original transaction identifier on partner system | 
**original_external_id** | **str** | Original external identifier on header message | [optional] 
**cancel_time** | **str** | Cancellation date time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time). Present if successfully processed | [optional] 
**transaction_date** | **str** | Transaction date, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | [optional] 
**additional_info** | **object** | Additional information | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.cancel_order_response import CancelOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelOrderResponse from a JSON string
cancel_order_response_instance = CancelOrderResponse.from_json(json)
# print the JSON string representation of the object
print(CancelOrderResponse.to_json())

# convert the object into a dict
cancel_order_response_dict = cancel_order_response_instance.to_dict()
# create an instance of CancelOrderResponse from a dict
cancel_order_response_from_dict = CancelOrderResponse.from_dict(cancel_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


