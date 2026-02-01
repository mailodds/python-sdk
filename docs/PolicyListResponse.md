# PolicyListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 
**limits** | [**PolicyListResponseLimits**](PolicyListResponseLimits.md) |  | [optional] 

## Example

```python
from mailodds.models.policy_list_response import PolicyListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyListResponse from a JSON string
policy_list_response_instance = PolicyListResponse.from_json(json)
# print the JSON string representation of the object
print(PolicyListResponse.to_json())

# convert the object into a dict
policy_list_response_dict = policy_list_response_instance.to_dict()
# create an instance of PolicyListResponse from a dict
policy_list_response_from_dict = PolicyListResponse.from_dict(policy_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


