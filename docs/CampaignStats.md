# CampaignStats

Delivery and engagement statistics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent** | **int** |  | [optional] 
**delivered** | **int** |  | [optional] 
**opened** | **int** |  | [optional] 
**clicked** | **int** |  | [optional] 
**bounced** | **int** |  | [optional] 
**unsubscribed** | **int** |  | [optional] 
**suppressed** | **int** |  | [optional] 
**failed** | **int** |  | [optional] 
**conversions** | **int** |  | [optional] 

## Example

```python
from mailodds.models.campaign_stats import CampaignStats

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignStats from a JSON string
campaign_stats_instance = CampaignStats.from_json(json)
# print the JSON string representation of the object
print(CampaignStats.to_json())

# convert the object into a dict
campaign_stats_dict = campaign_stats_instance.to_dict()
# create an instance of CampaignStats from a dict
campaign_stats_from_dict = CampaignStats.from_dict(campaign_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


