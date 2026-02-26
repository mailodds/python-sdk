# ConfirmSubscription200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**list_id** | **str** |  | [optional] 

## Example

```python
from mailodds.models.confirm_subscription200_response import ConfirmSubscription200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmSubscription200Response from a JSON string
confirm_subscription200_response_instance = ConfirmSubscription200Response.from_json(json)
# print the JSON string representation of the object
print(ConfirmSubscription200Response.to_json())

# convert the object into a dict
confirm_subscription200_response_dict = confirm_subscription200_response_instance.to_dict()
# create an instance of ConfirmSubscription200Response from a dict
confirm_subscription200_response_from_dict = ConfirmSubscription200Response.from_dict(confirm_subscription200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


