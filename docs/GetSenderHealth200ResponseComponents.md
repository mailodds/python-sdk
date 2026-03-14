# GetSenderHealth200ResponseComponents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_rate** | [**GetSenderHealth200ResponseComponentsDeliveryRate**](GetSenderHealth200ResponseComponentsDeliveryRate.md) |  | [optional] 
**bounce_rate** | [**GetSenderHealth200ResponseComponentsDeliveryRate**](GetSenderHealth200ResponseComponentsDeliveryRate.md) |  | [optional] 
**complaint_rate** | [**GetSenderHealth200ResponseComponentsDeliveryRate**](GetSenderHealth200ResponseComponentsDeliveryRate.md) |  | [optional] 
**authentication** | [**GetSenderHealth200ResponseComponentsDeliveryRate**](GetSenderHealth200ResponseComponentsDeliveryRate.md) |  | [optional] 

## Example

```python
from mailodds.models.get_sender_health200_response_components import GetSenderHealth200ResponseComponents

# TODO update the JSON string below
json = "{}"
# create an instance of GetSenderHealth200ResponseComponents from a JSON string
get_sender_health200_response_components_instance = GetSenderHealth200ResponseComponents.from_json(json)
# print the JSON string representation of the object
print(GetSenderHealth200ResponseComponents.to_json())

# convert the object into a dict
get_sender_health200_response_components_dict = get_sender_health200_response_components_instance.to_dict()
# create an instance of GetSenderHealth200ResponseComponents from a dict
get_sender_health200_response_components_from_dict = GetSenderHealth200ResponseComponents.from_dict(get_sender_health200_response_components_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


