# ValidationResponseSuppressionMatch

Present only when email matched a suppression list entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_type** | **str** |  | [optional] 
**match_value** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from mailodds.models.validation_response_suppression_match import ValidationResponseSuppressionMatch

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationResponseSuppressionMatch from a JSON string
validation_response_suppression_match_instance = ValidationResponseSuppressionMatch.from_json(json)
# print the JSON string representation of the object
print(ValidationResponseSuppressionMatch.to_json())

# convert the object into a dict
validation_response_suppression_match_dict = validation_response_suppression_match_instance.to_dict()
# create an instance of ValidationResponseSuppressionMatch from a dict
validation_response_suppression_match_from_dict = ValidationResponseSuppressionMatch.from_dict(validation_response_suppression_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


