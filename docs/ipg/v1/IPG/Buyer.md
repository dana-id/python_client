# Buyer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_user_type** | **str** | Type of external user. Required if externalUserId is filled | [optional] 
**nickname** | **str** | Nickname, user&#39;s nick name in DANA&#39;s | [optional] 
**external_user_id** | **str** | External user identifier. Required if externalUserType is filled | [optional] 
**user_id** | **str** | DANA&#39;s user identifier | [optional] 

## Example

```python
from dana.ipg.v1.models.buyer import Buyer

# TODO update the JSON string below
json = "{}"
# create an instance of Buyer from a JSON string
buyer_instance = Buyer.from_json(json)
# print the JSON string representation of the object
print(Buyer.to_json())

# convert the object into a dict
buyer_dict = buyer_instance.to_dict()
# create an instance of Buyer from a dict
buyer_from_dict = Buyer.from_dict(buyer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


