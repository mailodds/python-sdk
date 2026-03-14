# GetDmarcTrend200ResponseTrendInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**var_pass** | **int** |  | [optional] 
**fail** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**pass_rate** | **float** |  | [optional] 

## Example

```python
from mailodds.models.get_dmarc_trend200_response_trend_inner import GetDmarcTrend200ResponseTrendInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDmarcTrend200ResponseTrendInner from a JSON string
get_dmarc_trend200_response_trend_inner_instance = GetDmarcTrend200ResponseTrendInner.from_json(json)
# print the JSON string representation of the object
print(GetDmarcTrend200ResponseTrendInner.to_json())

# convert the object into a dict
get_dmarc_trend200_response_trend_inner_dict = get_dmarc_trend200_response_trend_inner_instance.to_dict()
# create an instance of GetDmarcTrend200ResponseTrendInner from a dict
get_dmarc_trend200_response_trend_inner_from_dict = GetDmarcTrend200ResponseTrendInner.from_dict(get_dmarc_trend200_response_trend_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


