# GetCampaignFunnel200ResponseFunnel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent** | **int** |  | [optional] 
**delivered** | **int** |  | [optional] 
**opened** | **int** |  | [optional] 
**clicked** | **int** |  | [optional] 
**unsubscribed** | **int** |  | [optional] 
**bounced** | **int** |  | [optional] 
**complained** | **int** |  | [optional] 

## Example

```python
from mailodds.models.get_campaign_funnel200_response_funnel import GetCampaignFunnel200ResponseFunnel

# TODO update the JSON string below
json = "{}"
# create an instance of GetCampaignFunnel200ResponseFunnel from a JSON string
get_campaign_funnel200_response_funnel_instance = GetCampaignFunnel200ResponseFunnel.from_json(json)
# print the JSON string representation of the object
print(GetCampaignFunnel200ResponseFunnel.to_json())

# convert the object into a dict
get_campaign_funnel200_response_funnel_dict = get_campaign_funnel200_response_funnel_instance.to_dict()
# create an instance of GetCampaignFunnel200ResponseFunnel from a dict
get_campaign_funnel200_response_funnel_from_dict = GetCampaignFunnel200ResponseFunnel.from_dict(get_campaign_funnel200_response_funnel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


