# PolicyPresetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**presets** | [**List[PolicyPresetsResponsePresetsInner]**](PolicyPresetsResponsePresetsInner.md) |  | [optional] 

## Example

```python
from mailodds.models.policy_presets_response import PolicyPresetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyPresetsResponse from a JSON string
policy_presets_response_instance = PolicyPresetsResponse.from_json(json)
# print the JSON string representation of the object
print(PolicyPresetsResponse.to_json())

# convert the object into a dict
policy_presets_response_dict = policy_presets_response_instance.to_dict()
# create an instance of PolicyPresetsResponse from a dict
policy_presets_response_from_dict = PolicyPresetsResponse.from_dict(policy_presets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


