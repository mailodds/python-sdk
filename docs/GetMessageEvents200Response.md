# GetMessageEvents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**message_id** | **str** |  | [optional] 
**recipient** | **str** |  | [optional] 
**summary** | [**GetMessageEvents200ResponseSummary**](GetMessageEvents200ResponseSummary.md) |  | [optional] 
**clicks** | [**List[GetMessageEvents200ResponseClicksInner]**](GetMessageEvents200ResponseClicksInner.md) |  | [optional] 
**events** | [**List[GetMessageEvents200ResponseEventsInner]**](GetMessageEvents200ResponseEventsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mailodds.models.get_message_events200_response import GetMessageEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessageEvents200Response from a JSON string
get_message_events200_response_instance = GetMessageEvents200Response.from_json(json)
# print the JSON string representation of the object
print(GetMessageEvents200Response.to_json())

# convert the object into a dict
get_message_events200_response_dict = get_message_events200_response_instance.to_dict()
# create an instance of GetMessageEvents200Response from a dict
get_message_events200_response_from_dict = GetMessageEvents200Response.from_dict(get_message_events200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


