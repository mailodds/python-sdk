# JobArtifacts

Download URLs for completed jobs. Present only when status is completed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csv_all** | **str** | CSV with all results | [optional] 
**csv_valid** | **str** | CSV with valid emails only | [optional] 
**csv_invalid** | **str** | CSV with invalid emails only | [optional] 

## Example

```python
from mailodds.models.job_artifacts import JobArtifacts

# TODO update the JSON string below
json = "{}"
# create an instance of JobArtifacts from a JSON string
job_artifacts_instance = JobArtifacts.from_json(json)
# print the JSON string representation of the object
print(JobArtifacts.to_json())

# convert the object into a dict
job_artifacts_dict = job_artifacts_instance.to_dict()
# create an instance of JobArtifacts from a dict
job_artifacts_from_dict = JobArtifacts.from_dict(job_artifacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


