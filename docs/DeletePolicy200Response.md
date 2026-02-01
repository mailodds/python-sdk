# DeletePolicy200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **bool** |  | [optional] 
**policy_id** | **int** |  | [optional] 

## Example

```python
from mailodds.models.delete_policy200_response import DeletePolicy200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePolicy200Response from a JSON string
delete_policy200_response_instance = DeletePolicy200Response.from_json(json)
# print the JSON string representation of the object
print(DeletePolicy200Response.to_json())

# convert the object into a dict
delete_policy200_response_dict = delete_policy200_response_instance.to_dict()
# create an instance of DeletePolicy200Response from a dict
delete_policy200_response_from_dict = DeletePolicy200Response.from_dict(delete_policy200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


