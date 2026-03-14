# BlacklistMonitor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Monitor UUID | [optional] 
**target** | **str** | IP address or domain being monitored | [optional] 
**target_type** | **str** |  | [optional] 
**status** | **str** | Current status (clean, listed) | [optional] 
**listed_count** | **int** | Number of blacklists currently listing this target | [optional] 
**last_checked_at** | **datetime** |  | [optional] 
**latest_check** | [**BlacklistMonitorLatestCheck**](BlacklistMonitorLatestCheck.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.blacklist_monitor import BlacklistMonitor

# TODO update the JSON string below
json = "{}"
# create an instance of BlacklistMonitor from a JSON string
blacklist_monitor_instance = BlacklistMonitor.from_json(json)
# print the JSON string representation of the object
print(BlacklistMonitor.to_json())

# convert the object into a dict
blacklist_monitor_dict = blacklist_monitor_instance.to_dict()
# create an instance of BlacklistMonitor from a dict
blacklist_monitor_from_dict = BlacklistMonitor.from_dict(blacklist_monitor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


