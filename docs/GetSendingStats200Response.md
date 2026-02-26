# GetSendingStats200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stats** | [**GetSendingStats200ResponseStats**](GetSendingStats200ResponseStats.md) |  | [optional] 

## Example

```python
from mailodds.models.get_sending_stats200_response import GetSendingStats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSendingStats200Response from a JSON string
get_sending_stats200_response_instance = GetSendingStats200Response.from_json(json)
# print the JSON string representation of the object
print(GetSendingStats200Response.to_json())

# convert the object into a dict
get_sending_stats200_response_dict = get_sending_stats200_response_instance.to_dict()
# create an instance of GetSendingStats200Response from a dict
get_sending_stats200_response_from_dict = GetSendingStats200Response.from_dict(get_sending_stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


