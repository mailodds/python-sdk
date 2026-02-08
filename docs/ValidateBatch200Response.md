# ValidateBatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**total** | **int** |  | [optional] 
**summary** | [**ValidateBatch200ResponseSummary**](ValidateBatch200ResponseSummary.md) |  | [optional] 
**results** | [**List[ValidationResponse]**](ValidationResponse.md) |  | [optional] 

## Example

```python
from mailodds.models.validate_batch200_response import ValidateBatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateBatch200Response from a JSON string
validate_batch200_response_instance = ValidateBatch200Response.from_json(json)
# print the JSON string representation of the object
print(ValidateBatch200Response.to_json())

# convert the object into a dict
validate_batch200_response_dict = validate_batch200_response_instance.to_dict()
# create an instance of ValidateBatch200Response from a dict
validate_batch200_response_from_dict = ValidateBatch200Response.from_dict(validate_batch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


