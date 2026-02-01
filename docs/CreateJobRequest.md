# CreateJobRequest

Bulk jobs use the account's default validation policy. To use a specific policy, set it as default via the Policies API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** | List of emails to validate | 
**dedup** | **bool** | Remove duplicate emails | [optional] [default to False]
**metadata** | **object** | Custom metadata for the job | [optional] 
**webhook_url** | **str** | URL for completion webhook | [optional] 
**idempotency_key** | **str** | Unique key for idempotent requests | [optional] 

## Example

```python
from mailodds.models.create_job_request import CreateJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJobRequest from a JSON string
create_job_request_instance = CreateJobRequest.from_json(json)
# print the JSON string representation of the object
print(CreateJobRequest.to_json())

# convert the object into a dict
create_job_request_dict = create_job_request_instance.to_dict()
# create an instance of CreateJobRequest from a dict
create_job_request_from_dict = CreateJobRequest.from_dict(create_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


