# TestPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **int** |  | 
**test_result** | [**TestPolicyRequestTestResult**](TestPolicyRequestTestResult.md) |  | 

## Example

```python
from mailodds.models.test_policy_request import TestPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestPolicyRequest from a JSON string
test_policy_request_instance = TestPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(TestPolicyRequest.to_json())

# convert the object into a dict
test_policy_request_dict = test_policy_request_instance.to_dict()
# create an instance of TestPolicyRequest from a dict
test_policy_request_from_dict = TestPolicyRequest.from_dict(test_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


