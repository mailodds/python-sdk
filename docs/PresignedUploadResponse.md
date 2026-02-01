# PresignedUploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**upload** | [**PresignedUploadResponseUpload**](PresignedUploadResponseUpload.md) |  | [optional] 

## Example

```python
from mailodds.models.presigned_upload_response import PresignedUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PresignedUploadResponse from a JSON string
presigned_upload_response_instance = PresignedUploadResponse.from_json(json)
# print the JSON string representation of the object
print(PresignedUploadResponse.to_json())

# convert the object into a dict
presigned_upload_response_dict = presigned_upload_response_instance.to_dict()
# create an instance of PresignedUploadResponse from a dict
presigned_upload_response_from_dict = PresignedUploadResponse.from_dict(presigned_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


