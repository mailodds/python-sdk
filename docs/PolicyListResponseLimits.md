# PolicyListResponseLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_policies** | **int** | -1 means unlimited | [optional] 
**max_rules_per_policy** | **int** |  | [optional] 
**plan** | **str** |  | [optional] 

## Example

```python
from mailodds.models.policy_list_response_limits import PolicyListResponseLimits

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyListResponseLimits from a JSON string
policy_list_response_limits_instance = PolicyListResponseLimits.from_json(json)
# print the JSON string representation of the object
print(PolicyListResponseLimits.to_json())

# convert the object into a dict
policy_list_response_limits_dict = policy_list_response_limits_instance.to_dict()
# create an instance of PolicyListResponseLimits from a dict
policy_list_response_limits_from_dict = PolicyListResponseLimits.from_dict(policy_list_response_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


