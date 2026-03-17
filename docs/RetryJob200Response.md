# RetryJob200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**job** | **object** |  | [optional] 
**pending_count** | **int** | Number of emails re-queued | [optional] 

## Example

```python
from mailodds.models.retry_job200_response import RetryJob200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RetryJob200Response from a JSON string
retry_job200_response_instance = RetryJob200Response.from_json(json)
# print the JSON string representation of the object
print(RetryJob200Response.to_json())

# convert the object into a dict
retry_job200_response_dict = retry_job200_response_instance.to_dict()
# create an instance of RetryJob200Response from a dict
retry_job200_response_from_dict = RetryJob200Response.from_dict(retry_job200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


