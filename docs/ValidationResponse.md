# ValidationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**email** | **str** |  | 
**status** | **str** | Validation status | 
**sub_status** | **str** | Detailed status reason | [optional] 
**action** | **str** | Recommended action | 
**domain** | **str** |  | [optional] 
**mx_found** | **bool** |  | [optional] 
**smtp_check** | **bool** |  | [optional] 
**disposable** | **bool** |  | [optional] 
**role_account** | **bool** |  | [optional] 
**free_provider** | **bool** |  | [optional] 
**suppression_match** | [**ValidationResponseSuppressionMatch**](ValidationResponseSuppressionMatch.md) |  | [optional] 

## Example

```python
from mailodds.models.validation_response import ValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationResponse from a JSON string
validation_response_instance = ValidationResponse.from_json(json)
# print the JSON string representation of the object
print(ValidationResponse.to_json())

# convert the object into a dict
validation_response_dict = validation_response_instance.to_dict()
# create an instance of ValidationResponse from a dict
validation_response_from_dict = ValidationResponse.from_dict(validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


