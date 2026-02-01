# ValidateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address to validate | 
**policy_id** | **int** | Optional policy ID to use instead of default policy | [optional] 

## Example

```python
from mailodds.models.validate_request import ValidateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateRequest from a JSON string
validate_request_instance = ValidateRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateRequest.to_json())

# convert the object into a dict
validate_request_dict = validate_request_instance.to_dict()
# create an instance of ValidateRequest from a dict
validate_request_from_dict = ValidateRequest.from_dict(validate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


