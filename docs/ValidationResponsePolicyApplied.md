# ValidationResponsePolicyApplied

Present when a validation policy modified the result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **int** |  | [optional] 
**policy_name** | **str** |  | [optional] 
**rule_id** | **int** |  | [optional] 
**rule_type** | **str** |  | [optional] 

## Example

```python
from mailodds.models.validation_response_policy_applied import ValidationResponsePolicyApplied

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationResponsePolicyApplied from a JSON string
validation_response_policy_applied_instance = ValidationResponsePolicyApplied.from_json(json)
# print the JSON string representation of the object
print(ValidationResponsePolicyApplied.to_json())

# convert the object into a dict
validation_response_policy_applied_dict = validation_response_policy_applied_instance.to_dict()
# create an instance of ValidationResponsePolicyApplied from a dict
validation_response_policy_applied_from_dict = ValidationResponsePolicyApplied.from_dict(validation_response_policy_applied_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


