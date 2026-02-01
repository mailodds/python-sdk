# TestPolicyRequestTestResult

Mock validation result to test against

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**sub_status** | **str** |  | [optional] 

## Example

```python
from mailodds.models.test_policy_request_test_result import TestPolicyRequestTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestPolicyRequestTestResult from a JSON string
test_policy_request_test_result_instance = TestPolicyRequestTestResult.from_json(json)
# print the JSON string representation of the object
print(TestPolicyRequestTestResult.to_json())

# convert the object into a dict
test_policy_request_test_result_dict = test_policy_request_test_result_instance.to_dict()
# create an instance of TestPolicyRequestTestResult from a dict
test_policy_request_test_result_from_dict = TestPolicyRequestTestResult.from_dict(test_policy_request_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


