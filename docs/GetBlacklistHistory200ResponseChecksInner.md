# GetBlacklistHistory200ResponseChecksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**listed_on** | **List[str]** |  | [optional] 
**clean_on** | **List[str]** |  | [optional] 
**checked_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.get_blacklist_history200_response_checks_inner import GetBlacklistHistory200ResponseChecksInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlacklistHistory200ResponseChecksInner from a JSON string
get_blacklist_history200_response_checks_inner_instance = GetBlacklistHistory200ResponseChecksInner.from_json(json)
# print the JSON string representation of the object
print(GetBlacklistHistory200ResponseChecksInner.to_json())

# convert the object into a dict
get_blacklist_history200_response_checks_inner_dict = get_blacklist_history200_response_checks_inner_instance.to_dict()
# create an instance of GetBlacklistHistory200ResponseChecksInner from a dict
get_blacklist_history200_response_checks_inner_from_dict = GetBlacklistHistory200ResponseChecksInner.from_dict(get_blacklist_history200_response_checks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


