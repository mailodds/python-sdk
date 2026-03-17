# ListSyncJobs200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**sync_jobs** | **List[object]** |  | [optional] 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 

## Example

```python
from mailodds.models.list_sync_jobs200_response import ListSyncJobs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSyncJobs200Response from a JSON string
list_sync_jobs200_response_instance = ListSyncJobs200Response.from_json(json)
# print the JSON string representation of the object
print(ListSyncJobs200Response.to_json())

# convert the object into a dict
list_sync_jobs200_response_dict = list_sync_jobs200_response_instance.to_dict()
# create an instance of ListSyncJobs200Response from a dict
list_sync_jobs200_response_from_dict = ListSyncJobs200Response.from_dict(list_sync_jobs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


