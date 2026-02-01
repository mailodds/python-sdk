# SuppressionStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**total** | **int** |  | [optional] 
**by_type** | [**SuppressionStatsResponseByType**](SuppressionStatsResponseByType.md) |  | [optional] 

## Example

```python
from mailodds.models.suppression_stats_response import SuppressionStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressionStatsResponse from a JSON string
suppression_stats_response_instance = SuppressionStatsResponse.from_json(json)
# print the JSON string representation of the object
print(SuppressionStatsResponse.to_json())

# convert the object into a dict
suppression_stats_response_dict = suppression_stats_response_instance.to_dict()
# create an instance of SuppressionStatsResponse from a dict
suppression_stats_response_from_dict = SuppressionStatsResponse.from_dict(suppression_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


