# CreateToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 
**expires_in** | **int** | Token lifetime in seconds | [optional] 
**refresh_token** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 

## Example

```python
from mailodds.models.create_token200_response import CreateToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateToken200Response from a JSON string
create_token200_response_instance = CreateToken200Response.from_json(json)
# print the JSON string representation of the object
print(CreateToken200Response.to_json())

# convert the object into a dict
create_token200_response_dict = create_token200_response_instance.to_dict()
# create an instance of CreateToken200Response from a dict
create_token200_response_from_dict = CreateToken200Response.from_dict(create_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


