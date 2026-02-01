# SuppressionCheckResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**suppressed** | **bool** |  | [optional] 
**match_type** | **str** |  | [optional] 
**match_value** | **str** |  | [optional] 

## Example

```python
from mailodds.models.suppression_check_response import SuppressionCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressionCheckResponse from a JSON string
suppression_check_response_instance = SuppressionCheckResponse.from_json(json)
# print the JSON string representation of the object
print(SuppressionCheckResponse.to_json())

# convert the object into a dict
suppression_check_response_dict = suppression_check_response_instance.to_dict()
# create an instance of SuppressionCheckResponse from a dict
suppression_check_response_from_dict = SuppressionCheckResponse.from_dict(suppression_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


