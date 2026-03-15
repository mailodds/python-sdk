# TrackEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | Type of commerce event | 
**email** | **str** | Email address associated with the event | 
**properties** | **object** | Event-specific data (e.g., order_id, value, product_url) | [optional] 
**occurred_at** | **datetime** | When the event occurred (defaults to now) | [optional] 
**idempotency_key** | **str** | Unique key to prevent duplicate events (5 min TTL) | [optional] 

## Example

```python
from mailodds.models.track_event_request import TrackEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackEventRequest from a JSON string
track_event_request_instance = TrackEventRequest.from_json(json)
# print the JSON string representation of the object
print(TrackEventRequest.to_json())

# convert the object into a dict
track_event_request_dict = track_event_request_instance.to_dict()
# create an instance of TrackEventRequest from a dict
track_event_request_from_dict = TrackEventRequest.from_dict(track_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


