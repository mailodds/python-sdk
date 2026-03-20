# GetBounceStats200ResponseStats

Bounce statistics with time-series data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **str** |  | [optional] 
**group_by** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from mailodds.models.get_bounce_stats200_response_stats import GetBounceStats200ResponseStats

# TODO update the JSON string below
json = "{}"
# create an instance of GetBounceStats200ResponseStats from a JSON string
get_bounce_stats200_response_stats_instance = GetBounceStats200ResponseStats.from_json(json)
# print the JSON string representation of the object
print(GetBounceStats200ResponseStats.to_json())

# convert the object into a dict
get_bounce_stats200_response_stats_dict = get_bounce_stats200_response_stats_instance.to_dict()
# create an instance of GetBounceStats200ResponseStats from a dict
get_bounce_stats200_response_stats_from_dict = GetBounceStats200ResponseStats.from_dict(get_bounce_stats200_response_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


