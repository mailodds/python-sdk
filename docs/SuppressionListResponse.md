# SuppressionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**entries** | [**List[SuppressionEntry]**](SuppressionEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from mailodds.models.suppression_list_response import SuppressionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressionListResponse from a JSON string
suppression_list_response_instance = SuppressionListResponse.from_json(json)
# print the JSON string representation of the object
print(SuppressionListResponse.to_json())

# convert the object into a dict
suppression_list_response_dict = suppression_list_response_instance.to_dict()
# create an instance of SuppressionListResponse from a dict
suppression_list_response_from_dict = SuppressionListResponse.from_dict(suppression_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


