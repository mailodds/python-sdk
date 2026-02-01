# SuppressionStatsResponseByType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **int** |  | [optional] 
**domain** | **int** |  | [optional] 

## Example

```python
from mailodds.models.suppression_stats_response_by_type import SuppressionStatsResponseByType

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressionStatsResponseByType from a JSON string
suppression_stats_response_by_type_instance = SuppressionStatsResponseByType.from_json(json)
# print the JSON string representation of the object
print(SuppressionStatsResponseByType.to_json())

# convert the object into a dict
suppression_stats_response_by_type_dict = suppression_stats_response_by_type_instance.to_dict()
# create an instance of SuppressionStatsResponseByType from a dict
suppression_stats_response_by_type_from_dict = SuppressionStatsResponseByType.from_dict(suppression_stats_response_by_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


