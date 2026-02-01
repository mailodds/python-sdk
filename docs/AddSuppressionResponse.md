# AddSuppressionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**added** | **int** |  | [optional] 
**skipped** | **int** |  | [optional] 

## Example

```python
from mailodds.models.add_suppression_response import AddSuppressionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddSuppressionResponse from a JSON string
add_suppression_response_instance = AddSuppressionResponse.from_json(json)
# print the JSON string representation of the object
print(AddSuppressionResponse.to_json())

# convert the object into a dict
add_suppression_response_dict = add_suppression_response_instance.to_dict()
# create an instance of AddSuppressionResponse from a dict
add_suppression_response_from_dict = AddSuppressionResponse.from_dict(add_suppression_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


