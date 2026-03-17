# GetReputationTimeline200ResponseTimelineTimelineInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**sent** | **int** |  | [optional] 
**bounce_rate** | **float** |  | [optional] 
**complaint_rate** | **float** |  | [optional] 
**open_rate** | **float** |  | [optional] 
**delivery_rate** | **float** |  | [optional] 

## Example

```python
from mailodds.models.get_reputation_timeline200_response_timeline_timeline_inner import GetReputationTimeline200ResponseTimelineTimelineInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReputationTimeline200ResponseTimelineTimelineInner from a JSON string
get_reputation_timeline200_response_timeline_timeline_inner_instance = GetReputationTimeline200ResponseTimelineTimelineInner.from_json(json)
# print the JSON string representation of the object
print(GetReputationTimeline200ResponseTimelineTimelineInner.to_json())

# convert the object into a dict
get_reputation_timeline200_response_timeline_timeline_inner_dict = get_reputation_timeline200_response_timeline_timeline_inner_instance.to_dict()
# create an instance of GetReputationTimeline200ResponseTimelineTimelineInner from a dict
get_reputation_timeline200_response_timeline_timeline_inner_from_dict = GetReputationTimeline200ResponseTimelineTimelineInner.from_dict(get_reputation_timeline200_response_timeline_timeline_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


