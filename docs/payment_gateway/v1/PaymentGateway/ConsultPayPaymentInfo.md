# ConsultPayPaymentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_method** | **str** | Payment method that used to payment. The enums:<br />   * BALANCE - Payment method with balance<br />   * COUPON - Payment method with coupon<br />   * NET_BANKING - Payment method with internet banking<br />   * CREDIT_CARD - Payment method with credit card<br />   * DEBIT_CARD - Payment method with debit card<br />   * VIRTUAL_ACCOUNT - Payment method with virtual account<br />   * OTC - Payment method with OTC<br />   * DIRECT_DEBIT_CREDIT_CARD - Payment method with direct debit of credit card<br />   * DIRECT_DEBIT_DEBIT_CARD - Payment method with direct debit of debit card<br />   * ONLINE_CREDIT - Payment method with online Credit<br />   * LOAN_CREDIT - Payment method with DANA Cicil<br />   * NETWORK_PAY - Payment method with e-wallet<br />  | 
**pay_option** | **str** | Payment option that available to used to payment, depends on the payment method. The enums:<br />   * NETWORK_PAY_PG_SPAY - Payment method with ShopeePay e-wallet<br />   * NETWORK_PAY_PG_OVO - Payment method with OVO e-wallet<br />   * NETWORK_PAY_PG_GOPAY - Payment method with GoPay e-wallet<br />   * NETWORK_PAY_PG_LINKAJA - Payment method with LinkAja e-wallet<br />   * NETWORK_PAY_PG_CARD - Payment method with Card<br />   * VIRTUAL_ACCOUNT_BCA - Payment method with BCA virtual account<br />   * VIRTUAL_ACCOUNT_BNI - Payment method with BNI virtual account<br />   * VIRTUAL_ACCOUNT_MANDIRI - Payment method with Mandiri virtual account<br />   * VIRTUAL_ACCOUNT_BRI - Payment method with BRI virtual account<br />   * VIRTUAL_ACCOUNT_BTPN - Payment method with BTPN virtual account<br />   * VIRTUAL_ACCOUNT_CIMB - Payment method with CIMB virtual account<br />   * VIRTUAL_ACCOUNT_PERMATA - Payment method with Permata virtual account<br />  | [optional] 
**promo_infos** | [**List[PromoInfo]**](PromoInfo.md) | Additional Information of promotion | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.consult_pay_payment_info import ConsultPayPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConsultPayPaymentInfo from a JSON string
consult_pay_payment_info_instance = ConsultPayPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(ConsultPayPaymentInfo.to_json())

# convert the object into a dict
consult_pay_payment_info_dict = consult_pay_payment_info_instance.to_dict()
# create an instance of ConsultPayPaymentInfo from a dict
consult_pay_payment_info_from_dict = ConsultPayPaymentInfo.from_dict(consult_pay_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


