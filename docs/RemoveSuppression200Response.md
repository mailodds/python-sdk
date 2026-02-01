# RemoveSuppression200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**removed** | **int** |  | [optional] 

## Example

```python
from mailodds.models.remove_suppression200_response import RemoveSuppression200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveSuppression200Response from a JSON string
remove_suppression200_response_instance = RemoveSuppression200Response.from_json(json)
# print the JSON string representation of the object
print(RemoveSuppression200Response.to_json())

# convert the object into a dict
remove_suppression200_response_dict = remove_suppression200_response_instance.to_dict()
# create an instance of RemoveSuppression200Response from a dict
remove_suppression200_response_from_dict = RemoveSuppression200Response.from_dict(remove_suppression200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


