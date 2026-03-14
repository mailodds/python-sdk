# RunBlacklistCheck200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**monitor** | [**BlacklistMonitor**](BlacklistMonitor.md) |  | [optional] 
**check** | [**RunBlacklistCheck200ResponseCheck**](RunBlacklistCheck200ResponseCheck.md) |  | [optional] 

## Example

```python
from mailodds.models.run_blacklist_check200_response import RunBlacklistCheck200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RunBlacklistCheck200Response from a JSON string
run_blacklist_check200_response_instance = RunBlacklistCheck200Response.from_json(json)
# print the JSON string representation of the object
print(RunBlacklistCheck200Response.to_json())

# convert the object into a dict
run_blacklist_check200_response_dict = run_blacklist_check200_response_instance.to_dict()
# create an instance of RunBlacklistCheck200Response from a dict
run_blacklist_check200_response_from_dict = RunBlacklistCheck200Response.from_dict(run_blacklist_check200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


