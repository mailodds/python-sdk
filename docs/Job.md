# Job


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | Job name (from metadata or auto-generated) | 
**status** | **str** |  | 
**total_count** | **int** |  | 
**processed_count** | **int** |  | 
**summary** | [**JobSummary**](JobSummary.md) |  | [optional] 
**created_at** | **datetime** |  | 
**started_at** | **datetime** | When processing began. Omitted if not yet started. | [optional] 
**completed_at** | **datetime** | Omitted if not yet completed. | [optional] 
**results_expire_at** | **datetime** | When job results will be purged | 
**metadata** | **object** | Custom metadata attached at creation | [optional] 
**error_message** | **str** | Error details. Present only for failed jobs. | [optional] 
**request_id** | **str** | Request ID from the job creation request | [optional] 
**artifacts** | [**JobArtifacts**](JobArtifacts.md) |  | [optional] 

## Example

```python
from mailodds.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print(Job.to_json())

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_from_dict = Job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


