# ClassifyContentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Email subject line | [optional] 
**html_body** | **str** | HTML email body | [optional] 
**content** | **str** | Raw text content (alternative to subject+html_body) | [optional] 

## Example

```python
from mailodds.models.classify_content_request import ClassifyContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClassifyContentRequest from a JSON string
classify_content_request_instance = ClassifyContentRequest.from_json(json)
# print the JSON string representation of the object
print(ClassifyContentRequest.to_json())

# convert the object into a dict
classify_content_request_dict = classify_content_request_instance.to_dict()
# create an instance of ClassifyContentRequest from a dict
classify_content_request_from_dict = ClassifyContentRequest.from_dict(classify_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


