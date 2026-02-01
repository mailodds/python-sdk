# PolicyPresetsResponsePresetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**rules** | [**List[PolicyRule]**](PolicyRule.md) |  | [optional] 

## Example

```python
from mailodds.models.policy_presets_response_presets_inner import PolicyPresetsResponsePresetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyPresetsResponsePresetsInner from a JSON string
policy_presets_response_presets_inner_instance = PolicyPresetsResponsePresetsInner.from_json(json)
# print the JSON string representation of the object
print(PolicyPresetsResponsePresetsInner.to_json())

# convert the object into a dict
policy_presets_response_presets_inner_dict = policy_presets_response_presets_inner_instance.to_dict()
# create an instance of PolicyPresetsResponsePresetsInner from a dict
policy_presets_response_presets_inner_from_dict = PolicyPresetsResponsePresetsInner.from_dict(policy_presets_response_presets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


