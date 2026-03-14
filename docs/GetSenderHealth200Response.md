# GetSenderHealth200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** | Unique request identifier | [optional] 
**score** | **int** | Overall sender health score (0-100) | [optional] 
**grade** | **str** | Letter grade based on score | [optional] 
**period** | **str** |  | [optional] 
**components** | [**GetSenderHealth200ResponseComponents**](GetSenderHealth200ResponseComponents.md) |  | [optional] 
**volume** | [**GetSenderHealth200ResponseVolume**](GetSenderHealth200ResponseVolume.md) |  | [optional] 

## Example

```python
from mailodds.models.get_sender_health200_response import GetSenderHealth200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSenderHealth200Response from a JSON string
get_sender_health200_response_instance = GetSenderHealth200Response.from_json(json)
# print the JSON string representation of the object
print(GetSenderHealth200Response.to_json())

# convert the object into a dict
get_sender_health200_response_dict = get_sender_health200_response_instance.to_dict()
# create an instance of GetSenderHealth200Response from a dict
get_sender_health200_response_from_dict = GetSenderHealth200Response.from_dict(get_sender_health200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


