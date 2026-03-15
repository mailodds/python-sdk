# IntrospectToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | 
**scope** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 
**exp** | **int** |  | [optional] 
**iat** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 

## Example

```python
from mailodds.models.introspect_token200_response import IntrospectToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of IntrospectToken200Response from a JSON string
introspect_token200_response_instance = IntrospectToken200Response.from_json(json)
# print the JSON string representation of the object
print(IntrospectToken200Response.to_json())

# convert the object into a dict
introspect_token200_response_dict = introspect_token200_response_instance.to_dict()
# create an instance of IntrospectToken200Response from a dict
introspect_token200_response_from_dict = IntrospectToken200Response.from_dict(introspect_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


