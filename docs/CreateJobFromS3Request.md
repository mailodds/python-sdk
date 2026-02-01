# CreateJobFromS3Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s3_key** | **str** | S3 key from presigned upload | 
**dedup** | **bool** |  | [optional] [default to False]

## Example

```python
from mailodds.models.create_job_from_s3_request import CreateJobFromS3Request

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJobFromS3Request from a JSON string
create_job_from_s3_request_instance = CreateJobFromS3Request.from_json(json)
# print the JSON string representation of the object
print(CreateJobFromS3Request.to_json())

# convert the object into a dict
create_job_from_s3_request_dict = create_job_from_s3_request_instance.to_dict()
# create an instance of CreateJobFromS3Request from a dict
create_job_from_s3_request_from_dict = CreateJobFromS3Request.from_dict(create_job_from_s3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


