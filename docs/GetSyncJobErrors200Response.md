# GetSyncJobErrors200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**errors** | **List[object]** |  | [optional] 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 

## Example

```python
from mailodds.models.get_sync_job_errors200_response import GetSyncJobErrors200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSyncJobErrors200Response from a JSON string
get_sync_job_errors200_response_instance = GetSyncJobErrors200Response.from_json(json)
# print the JSON string representation of the object
print(GetSyncJobErrors200Response.to_json())

# convert the object into a dict
get_sync_job_errors200_response_dict = get_sync_job_errors200_response_instance.to_dict()
# create an instance of GetSyncJobErrors200Response from a dict
get_sync_job_errors200_response_from_dict = GetSyncJobErrors200Response.from_dict(get_sync_job_errors200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


