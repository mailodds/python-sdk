# ClassifyContent200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**content_check** | [**ClassifyContent200ResponseContentCheck**](ClassifyContent200ResponseContentCheck.md) |  | [optional] 

## Example

```python
from mailodds.models.classify_content200_response import ClassifyContent200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClassifyContent200Response from a JSON string
classify_content200_response_instance = ClassifyContent200Response.from_json(json)
# print the JSON string representation of the object
print(ClassifyContent200Response.to_json())

# convert the object into a dict
classify_content200_response_dict = classify_content200_response_instance.to_dict()
# create an instance of ClassifyContent200Response from a dict
classify_content200_response_from_dict = ClassifyContent200Response.from_dict(classify_content200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


