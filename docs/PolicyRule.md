# PolicyRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** | Rule type determines how condition is evaluated | 
**condition** | **object** | Condition depends on rule type. status_override: {status}, domain_filter: {domain_mode, domains}, check_requirement: {check, required}, sub_status_override: {sub_status} | 
**action** | [**PolicyRuleAction**](PolicyRuleAction.md) |  | 
**sequence** | **int** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 

## Example

```python
from mailodds.models.policy_rule import PolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRule from a JSON string
policy_rule_instance = PolicyRule.from_json(json)
# print the JSON string representation of the object
print(PolicyRule.to_json())

# convert the object into a dict
policy_rule_dict = policy_rule_instance.to_dict()
# create an instance of PolicyRule from a dict
policy_rule_from_dict = PolicyRule.from_dict(policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


