# AddBlacklistMonitorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | IP address or domain to monitor | 
**target_type** | **str** | Whether the target is an IP or domain | 

## Example

```python
from mailodds.models.add_blacklist_monitor_request import AddBlacklistMonitorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddBlacklistMonitorRequest from a JSON string
add_blacklist_monitor_request_instance = AddBlacklistMonitorRequest.from_json(json)
# print the JSON string representation of the object
print(AddBlacklistMonitorRequest.to_json())

# convert the object into a dict
add_blacklist_monitor_request_dict = add_blacklist_monitor_request_instance.to_dict()
# create an instance of AddBlacklistMonitorRequest from a dict
add_blacklist_monitor_request_from_dict = AddBlacklistMonitorRequest.from_dict(add_blacklist_monitor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


