# ClassifyContent200ResponseContentCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** | Overall content quality score (0-100) | [optional] 
**verdict** | **str** | Overall verdict | [optional] 
**categories** | [**List[ClassifyContent200ResponseContentCheckCategoriesInner]**](ClassifyContent200ResponseContentCheckCategoriesInner.md) |  | [optional] 
**suggestions** | **List[str]** | Improvement suggestions | [optional] 

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


