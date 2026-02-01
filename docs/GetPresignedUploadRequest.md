# GetPresignedUploadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | Original filename | 
**content_type** | **str** | File MIME type | [optional] 

## Example

```python
from mailodds.models.get_presigned_upload_request import GetPresignedUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPresignedUploadRequest from a JSON string
get_presigned_upload_request_instance = GetPresignedUploadRequest.from_json(json)
# print the JSON string representation of the object
print(GetPresignedUploadRequest.to_json())

# convert the object into a dict
get_presigned_upload_request_dict = get_presigned_upload_request_instance.to_dict()
# create an instance of GetPresignedUploadRequest from a dict
get_presigned_upload_request_from_dict = GetPresignedUploadRequest.from_dict(get_presigned_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


