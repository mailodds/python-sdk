# RunBlacklistCheck200ResponseCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**listed_on** | **List[str]** | Blacklists where the target is listed | [optional] 
**clean_on** | **List[str]** | Blacklists where the target is clean | [optional] 
**checked_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.run_blacklist_check200_response_check import RunBlacklistCheck200ResponseCheck

# TODO update the JSON string below
json = "{}"
# create an instance of RunBlacklistCheck200ResponseCheck from a JSON string
run_blacklist_check200_response_check_instance = RunBlacklistCheck200ResponseCheck.from_json(json)
# print the JSON string representation of the object
print(RunBlacklistCheck200ResponseCheck.to_json())

# convert the object into a dict
run_blacklist_check200_response_check_dict = run_blacklist_check200_response_check_instance.to_dict()
# create an instance of RunBlacklistCheck200ResponseCheck from a dict
run_blacklist_check200_response_check_from_dict = RunBlacklistCheck200ResponseCheck.from_dict(run_blacklist_check200_response_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


