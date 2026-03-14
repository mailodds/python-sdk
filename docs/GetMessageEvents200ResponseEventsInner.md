# GetMessageEvents200ResponseEventsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**event_type** | **str** |  | [optional] 
**is_bot** | **bool** |  | [optional] 
**link_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.get_message_events200_response_events_inner import GetMessageEvents200ResponseEventsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessageEvents200ResponseEventsInner from a JSON string
get_message_events200_response_events_inner_instance = GetMessageEvents200ResponseEventsInner.from_json(json)
# print the JSON string representation of the object
print(GetMessageEvents200ResponseEventsInner.to_json())

# convert the object into a dict
get_message_events200_response_events_inner_dict = get_message_events200_response_events_inner_instance.to_dict()
# create an instance of GetMessageEvents200ResponseEventsInner from a dict
get_message_events200_response_events_inner_from_dict = GetMessageEvents200ResponseEventsInner.from_dict(get_message_events200_response_events_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


