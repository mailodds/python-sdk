# DisconnectStore200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**disconnected** | **bool** |  | [optional] 

## Example

```python
from mailodds.models.disconnect_store200_response import DisconnectStore200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DisconnectStore200Response from a JSON string
disconnect_store200_response_instance = DisconnectStore200Response.from_json(json)
# print the JSON string representation of the object
print(DisconnectStore200Response.to_json())

# convert the object into a dict
disconnect_store200_response_dict = disconnect_store200_response_instance.to_dict()
# create an instance of DisconnectStore200Response from a dict
disconnect_store200_response_from_dict = DisconnectStore200Response.from_dict(disconnect_store200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


