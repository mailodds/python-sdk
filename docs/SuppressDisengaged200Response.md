# SuppressDisengaged200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**suppressed_count** | **int** |  | [optional] 
**dry_run** | **bool** |  | [optional] 

## Example

```python
from mailodds.models.suppress_disengaged200_response import SuppressDisengaged200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressDisengaged200Response from a JSON string
suppress_disengaged200_response_instance = SuppressDisengaged200Response.from_json(json)
# print the JSON string representation of the object
print(SuppressDisengaged200Response.to_json())

# convert the object into a dict
suppress_disengaged200_response_dict = suppress_disengaged200_response_instance.to_dict()
# create an instance of SuppressDisengaged200Response from a dict
suppress_disengaged200_response_from_dict = SuppressDisengaged200Response.from_dict(suppress_disengaged200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


