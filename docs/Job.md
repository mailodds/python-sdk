# Job


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**total_count** | **int** |  | [optional] 
**processed_count** | **int** |  | [optional] 
**progress_percent** | **int** |  | [optional] 
**summary** | [**JobSummary**](JobSummary.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**metadata** | **object** |  | [optional] 

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


