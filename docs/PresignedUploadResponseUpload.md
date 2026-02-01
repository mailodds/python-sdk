# PresignedUploadResponseUpload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**fields** | **object** |  | [optional] 
**s3_key** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 

## Example

```python
from mailodds.models.presigned_upload_response_upload import PresignedUploadResponseUpload

# TODO update the JSON string below
json = "{}"
# create an instance of PresignedUploadResponseUpload from a JSON string
presigned_upload_response_upload_instance = PresignedUploadResponseUpload.from_json(json)
# print the JSON string representation of the object
print(PresignedUploadResponseUpload.to_json())

# convert the object into a dict
presigned_upload_response_upload_dict = presigned_upload_response_upload_instance.to_dict()
# create an instance of PresignedUploadResponseUpload from a dict
presigned_upload_response_upload_from_dict = PresignedUploadResponseUpload.from_dict(presigned_upload_response_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


