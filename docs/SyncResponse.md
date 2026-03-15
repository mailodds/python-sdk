# SyncResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**scheduled** | **bool** |  | [optional] 
**store_id** | **str** |  | [optional] 
**idempotent** | **bool** | True if this was a duplicate request matched by Idempotency-Key | [optional] 
**existing_job_id** | **str** | ID of existing sync job if one was already running | [optional] 

## Example

```python
from mailodds.models.sync_response import SyncResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyncResponse from a JSON string
sync_response_instance = SyncResponse.from_json(json)
# print the JSON string representation of the object
print(SyncResponse.to_json())

# convert the object into a dict
sync_response_dict = sync_response_instance.to_dict()
# create an instance of SyncResponse from a dict
sync_response_from_dict = SyncResponse.from_dict(sync_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


