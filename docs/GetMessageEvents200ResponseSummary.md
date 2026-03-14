# GetMessageEvents200ResponseSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivered** | **bool** |  | [optional] 
**bounced** | **bool** |  | [optional] 
**human_opens** | **int** |  | [optional] 
**bot_opens** | **int** |  | [optional] 
**clicks** | **int** |  | [optional] 
**unsubscribed** | **bool** |  | [optional] 

## Example

```python
from mailodds.models.get_message_events200_response_summary import GetMessageEvents200ResponseSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessageEvents200ResponseSummary from a JSON string
get_message_events200_response_summary_instance = GetMessageEvents200ResponseSummary.from_json(json)
# print the JSON string representation of the object
print(GetMessageEvents200ResponseSummary.to_json())

# convert the object into a dict
get_message_events200_response_summary_dict = get_message_events200_response_summary_instance.to_dict()
# create an instance of GetMessageEvents200ResponseSummary from a dict
get_message_events200_response_summary_from_dict = GetMessageEvents200ResponseSummary.from_dict(get_message_events200_response_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


