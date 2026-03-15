# ClassifyContent200ResponseContentCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Overall content status | [optional] 
**flag** | **bool** | Whether the content is flagged | [optional] 
**reason** | **str** | Human-readable reason for the status | [optional] 
**priority** | **int** | Priority level (1&#x3D;lowest, 5&#x3D;highest) | [optional] 
**suggestions** | **List[str]** | Improvement suggestions | [optional] 
**duration_ms** | **int** | Classification duration in milliseconds | [optional] 

## Example

```python
from mailodds.models.classify_content200_response_content_check import ClassifyContent200ResponseContentCheck

# TODO update the JSON string below
json = "{}"
# create an instance of ClassifyContent200ResponseContentCheck from a JSON string
classify_content200_response_content_check_instance = ClassifyContent200ResponseContentCheck.from_json(json)
# print the JSON string representation of the object
print(ClassifyContent200ResponseContentCheck.to_json())

# convert the object into a dict
classify_content200_response_content_check_dict = classify_content200_response_content_check_instance.to_dict()
# create an instance of ClassifyContent200ResponseContentCheck from a dict
classify_content200_response_content_check_from_dict = ClassifyContent200ResponseContentCheck.from_dict(classify_content200_response_content_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


