# PolicyTestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**original** | **object** | Original validation result before policy | [optional] 
**modified** | **object** | Result after policy applied | [optional] 
**matched_rule** | **object** | The rule that matched, or null if none matched | [optional] 
**rules_evaluated** | **int** |  | [optional] 

## Example

```python
from mailodds.models.policy_test_response import PolicyTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTestResponse from a JSON string
policy_test_response_instance = PolicyTestResponse.from_json(json)
# print the JSON string representation of the object
print(PolicyTestResponse.to_json())

# convert the object into a dict
policy_test_response_dict = policy_test_response_instance.to_dict()
# create an instance of PolicyTestResponse from a dict
policy_test_response_from_dict = PolicyTestResponse.from_dict(policy_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


