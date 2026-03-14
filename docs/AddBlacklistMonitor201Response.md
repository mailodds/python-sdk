# AddBlacklistMonitor201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**monitor** | [**BlacklistMonitor**](BlacklistMonitor.md) |  | [optional] 

## Example

```python
from mailodds.models.add_blacklist_monitor201_response import AddBlacklistMonitor201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddBlacklistMonitor201Response from a JSON string
add_blacklist_monitor201_response_instance = AddBlacklistMonitor201Response.from_json(json)
# print the JSON string representation of the object
print(AddBlacklistMonitor201Response.to_json())

# convert the object into a dict
add_blacklist_monitor201_response_dict = add_blacklist_monitor201_response_instance.to_dict()
# create an instance of AddBlacklistMonitor201Response from a dict
add_blacklist_monitor201_response_from_dict = AddBlacklistMonitor201Response.from_dict(add_blacklist_monitor201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


