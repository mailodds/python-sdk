# GetSenderHealthTrend200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** | Unique request identifier | [optional] 
**period** | **str** |  | [optional] 
**data_points** | [**List[GetSenderHealthTrend200ResponseDataPointsInner]**](GetSenderHealthTrend200ResponseDataPointsInner.md) |  | [optional] 

## Example

```python
from mailodds.models.get_sender_health_trend200_response import GetSenderHealthTrend200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSenderHealthTrend200Response from a JSON string
get_sender_health_trend200_response_instance = GetSenderHealthTrend200Response.from_json(json)
# print the JSON string representation of the object
print(GetSenderHealthTrend200Response.to_json())

# convert the object into a dict
get_sender_health_trend200_response_dict = get_sender_health_trend200_response_instance.to_dict()
# create an instance of GetSenderHealthTrend200Response from a dict
get_sender_health_trend200_response_from_dict = GetSenderHealthTrend200Response.from_dict(get_sender_health_trend200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


