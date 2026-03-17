# GetOooStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**is_ooo** | **bool** |  | [optional] 
**detected_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**ooo_type** | **str** |  | [optional] 

## Example

```python
from mailodds.models.get_ooo_status200_response import GetOooStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOooStatus200Response from a JSON string
get_ooo_status200_response_instance = GetOooStatus200Response.from_json(json)
# print the JSON string representation of the object
print(GetOooStatus200Response.to_json())

# convert the object into a dict
get_ooo_status200_response_dict = get_ooo_status200_response_instance.to_dict()
# create an instance of GetOooStatus200Response from a dict
get_ooo_status200_response_from_dict = GetOooStatus200Response.from_dict(get_ooo_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


