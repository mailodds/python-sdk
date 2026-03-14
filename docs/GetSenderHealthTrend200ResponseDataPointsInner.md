# GetSenderHealthTrend200ResponseDataPointsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**score** | **int** |  | [optional] 
**delivery_rate** | **float** |  | [optional] 
**bounce_rate** | **float** |  | [optional] 
**complaint_rate** | **float** |  | [optional] 
**volume** | **int** |  | [optional] 

## Example

```python
from mailodds.models.get_sender_health_trend200_response_data_points_inner import GetSenderHealthTrend200ResponseDataPointsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSenderHealthTrend200ResponseDataPointsInner from a JSON string
get_sender_health_trend200_response_data_points_inner_instance = GetSenderHealthTrend200ResponseDataPointsInner.from_json(json)
# print the JSON string representation of the object
print(GetSenderHealthTrend200ResponseDataPointsInner.to_json())

# convert the object into a dict
get_sender_health_trend200_response_data_points_inner_dict = get_sender_health_trend200_response_data_points_inner_instance.to_dict()
# create an instance of GetSenderHealthTrend200ResponseDataPointsInner from a dict
get_sender_health_trend200_response_data_points_inner_from_dict = GetSenderHealthTrend200ResponseDataPointsInner.from_dict(get_sender_health_trend200_response_data_points_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


