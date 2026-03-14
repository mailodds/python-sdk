# GetMessageEvents200ResponseClicksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**is_bot** | **bool** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.get_message_events200_response_clicks_inner import GetMessageEvents200ResponseClicksInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessageEvents200ResponseClicksInner from a JSON string
get_message_events200_response_clicks_inner_instance = GetMessageEvents200ResponseClicksInner.from_json(json)
# print the JSON string representation of the object
print(GetMessageEvents200ResponseClicksInner.to_json())

# convert the object into a dict
get_message_events200_response_clicks_inner_dict = get_message_events200_response_clicks_inner_instance.to_dict()
# create an instance of GetMessageEvents200ResponseClicksInner from a dict
get_message_events200_response_clicks_inner_from_dict = GetMessageEvents200ResponseClicksInner.from_dict(get_message_events200_response_clicks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


