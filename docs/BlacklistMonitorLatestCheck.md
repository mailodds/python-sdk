# BlacklistMonitorLatestCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**listed_on** | **List[str]** |  | [optional] 
**clean_on** | **List[str]** |  | [optional] 
**checked_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.blacklist_monitor_latest_check import BlacklistMonitorLatestCheck

# TODO update the JSON string below
json = "{}"
# create an instance of BlacklistMonitorLatestCheck from a JSON string
blacklist_monitor_latest_check_instance = BlacklistMonitorLatestCheck.from_json(json)
# print the JSON string representation of the object
print(BlacklistMonitorLatestCheck.to_json())

# convert the object into a dict
blacklist_monitor_latest_check_dict = blacklist_monitor_latest_check_instance.to_dict()
# create an instance of BlacklistMonitorLatestCheck from a dict
blacklist_monitor_latest_check_from_dict = BlacklistMonitorLatestCheck.from_dict(blacklist_monitor_latest_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


