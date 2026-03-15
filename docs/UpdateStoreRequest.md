# UpdateStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_name** | **str** | Display name for the store | [optional] 
**sync_interval_seconds** | **int** | Auto-sync interval in seconds (min 1800) | [optional] 
**settings** | **object** | Platform-specific settings | [optional] 
**credentials** | **object** | Updated store credentials (connection is tested before saving) | [optional] 

## Example

```python
from mailodds.models.update_store_request import UpdateStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStoreRequest from a JSON string
update_store_request_instance = UpdateStoreRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateStoreRequest.to_json())

# convert the object into a dict
update_store_request_dict = update_store_request_instance.to_dict()
# create an instance of UpdateStoreRequest from a dict
update_store_request_from_dict = UpdateStoreRequest.from_dict(update_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


