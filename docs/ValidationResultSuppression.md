# ValidationResultSuppression

Present only when email matched a suppression entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_type** | **str** |  | [optional] 
**match_value** | **str** |  | [optional] 

## Example

```python
from mailodds.models.validation_result_suppression import ValidationResultSuppression

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationResultSuppression from a JSON string
validation_result_suppression_instance = ValidationResultSuppression.from_json(json)
# print the JSON string representation of the object
print(ValidationResultSuppression.to_json())

# convert the object into a dict
validation_result_suppression_dict = validation_result_suppression_instance.to_dict()
# create an instance of ValidationResultSuppression from a dict
validation_result_suppression_from_dict = ValidationResultSuppression.from_dict(validation_result_suppression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


