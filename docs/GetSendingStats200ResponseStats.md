# GetSendingStats200ResponseStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **str** |  | [optional] 
**sent** | **int** |  | [optional] 
**delivered** | **int** |  | [optional] 
**bounced** | **int** |  | [optional] 
**deferred** | **int** |  | [optional] 
**failed** | **int** |  | [optional] 
**opened_total** | **int** |  | [optional] 
**opened_unique** | **int** |  | [optional] 
**clicked_total** | **int** |  | [optional] 
**clicked_unique** | **int** |  | [optional] 
**unsubscribed** | **int** |  | [optional] 
**delivery_rate** | **float** |  | [optional] 
**open_rate** | **float** |  | [optional] 
**click_rate** | **float** |  | [optional] 
**bot_opens** | **int** | Opens from known bots/scanners | [optional] 
**human_opens** | **int** | Verified human opens | [optional] 
**bot_open_pct** | **float** | Percentage of opens from bots | [optional] 

## Example

```python
from mailodds.models.get_sending_stats200_response_stats import GetSendingStats200ResponseStats

# TODO update the JSON string below
json = "{}"
# create an instance of GetSendingStats200ResponseStats from a JSON string
get_sending_stats200_response_stats_instance = GetSendingStats200ResponseStats.from_json(json)
# print the JSON string representation of the object
print(GetSendingStats200ResponseStats.to_json())

# convert the object into a dict
get_sending_stats200_response_stats_dict = get_sending_stats200_response_stats_instance.to_dict()
# create an instance of GetSendingStats200ResponseStats from a dict
get_sending_stats200_response_stats_from_dict = GetSendingStats200ResponseStats.from_dict(get_sending_stats200_response_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


