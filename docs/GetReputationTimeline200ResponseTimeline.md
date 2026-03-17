# GetReputationTimeline200ResponseTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **str** |  | [optional] 
**timeline** | [**List[GetReputationTimeline200ResponseTimelineTimelineInner]**](GetReputationTimeline200ResponseTimelineTimelineInner.md) |  | [optional] 

## Example

```python
from mailodds.models.get_reputation_timeline200_response_timeline import GetReputationTimeline200ResponseTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of GetReputationTimeline200ResponseTimeline from a JSON string
get_reputation_timeline200_response_timeline_instance = GetReputationTimeline200ResponseTimeline.from_json(json)
# print the JSON string representation of the object
print(GetReputationTimeline200ResponseTimeline.to_json())

# convert the object into a dict
get_reputation_timeline200_response_timeline_dict = get_reputation_timeline200_response_timeline_instance.to_dict()
# create an instance of GetReputationTimeline200ResponseTimeline from a dict
get_reputation_timeline200_response_timeline_from_dict = GetReputationTimeline200ResponseTimeline.from_dict(get_reputation_timeline200_response_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


