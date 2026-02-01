# AddPolicyRule201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | [**PolicyRule**](PolicyRule.md) |  | [optional] 

## Example

```python
from mailodds.models.add_policy_rule201_response import AddPolicyRule201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddPolicyRule201Response from a JSON string
add_policy_rule201_response_instance = AddPolicyRule201Response.from_json(json)
# print the JSON string representation of the object
print(AddPolicyRule201Response.to_json())

# convert the object into a dict
add_policy_rule201_response_dict = add_policy_rule201_response_instance.to_dict()
# create an instance of AddPolicyRule201Response from a dict
add_policy_rule201_response_from_dict = AddPolicyRule201Response.from_dict(add_policy_rule201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


