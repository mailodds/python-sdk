# TrackEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**event_id** | **int** | Event ID | [optional] 
**created** | **bool** | True if newly created, false if idempotent duplicate | [optional] 
**idempotent** | **bool** | Present and true when returning an existing event | [optional] 

## Example

```python
from mailodds.models.track_event_response import TrackEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrackEventResponse from a JSON string
track_event_response_instance = TrackEventResponse.from_json(json)
# print the JSON string representation of the object
print(TrackEventResponse.to_json())

# convert the object into a dict
track_event_response_dict = track_event_response_instance.to_dict()
# create an instance of TrackEventResponse from a dict
track_event_response_from_dict = TrackEventResponse.from_dict(track_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


