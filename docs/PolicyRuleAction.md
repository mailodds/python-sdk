# PolicyRuleAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 

## Example

```python
from mailodds.models.policy_rule_action import PolicyRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleAction from a JSON string
policy_rule_action_instance = PolicyRuleAction.from_json(json)
# print the JSON string representation of the object
print(PolicyRuleAction.to_json())

# convert the object into a dict
policy_rule_action_dict = policy_rule_action_instance.to_dict()
# create an instance of PolicyRuleAction from a dict
policy_rule_action_from_dict = PolicyRuleAction.from_dict(policy_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


