# GetBlacklistHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**checks** | [**List[GetBlacklistHistory200ResponseChecksInner]**](GetBlacklistHistory200ResponseChecksInner.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from mailodds.models.get_blacklist_history200_response import GetBlacklistHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlacklistHistory200Response from a JSON string
get_blacklist_history200_response_instance = GetBlacklistHistory200Response.from_json(json)
# print the JSON string representation of the object
print(GetBlacklistHistory200Response.to_json())

# convert the object into a dict
get_blacklist_history200_response_dict = get_blacklist_history200_response_instance.to_dict()
# create an instance of GetBlacklistHistory200Response from a dict
get_blacklist_history200_response_from_dict = GetBlacklistHistory200Response.from_dict(get_blacklist_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


