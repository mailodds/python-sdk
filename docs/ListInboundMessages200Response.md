# ListInboundMessages200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**messages** | **List[object]** |  | [optional] 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 

## Example

```python
from mailodds.models.list_inbound_messages200_response import ListInboundMessages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListInboundMessages200Response from a JSON string
list_inbound_messages200_response_instance = ListInboundMessages200Response.from_json(json)
# print the JSON string representation of the object
print(ListInboundMessages200Response.to_json())

# convert the object into a dict
list_inbound_messages200_response_dict = list_inbound_messages200_response_instance.to_dict()
# create an instance of ListInboundMessages200Response from a dict
list_inbound_messages200_response_from_dict = ListInboundMessages200Response.from_dict(list_inbound_messages200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


