# CreatePolicyFromPresetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preset_id** | **str** |  | 
**name** | **str** |  | 
**is_default** | **bool** |  | [optional] [default to False]

## Example

```python
from mailodds.models.create_policy_from_preset_request import CreatePolicyFromPresetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePolicyFromPresetRequest from a JSON string
create_policy_from_preset_request_instance = CreatePolicyFromPresetRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePolicyFromPresetRequest.to_json())

# convert the object into a dict
create_policy_from_preset_request_dict = create_policy_from_preset_request_instance.to_dict()
# create an instance of CreatePolicyFromPresetRequest from a dict
create_policy_from_preset_request_from_dict = CreatePolicyFromPresetRequest.from_dict(create_policy_from_preset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


