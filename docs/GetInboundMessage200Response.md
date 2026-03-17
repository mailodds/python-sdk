# GetInboundMessage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**message** | **object** |  | [optional] 

## Example

```python
from mailodds.models.get_inbound_message200_response import GetInboundMessage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetInboundMessage200Response from a JSON string
get_inbound_message200_response_instance = GetInboundMessage200Response.from_json(json)
# print the JSON string representation of the object
print(GetInboundMessage200Response.to_json())

# convert the object into a dict
get_inbound_message200_response_dict = get_inbound_message200_response_instance.to_dict()
# create an instance of GetInboundMessage200Response from a dict
get_inbound_message200_response_from_dict = GetInboundMessage200Response.from_dict(get_inbound_message200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


