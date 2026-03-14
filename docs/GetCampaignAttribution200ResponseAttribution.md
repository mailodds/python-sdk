# GetCampaignAttribution200ResponseAttribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_touch** | [**GetCampaignAttribution200ResponseAttributionFirstTouch**](GetCampaignAttribution200ResponseAttributionFirstTouch.md) |  | [optional] 
**last_touch** | [**GetCampaignAttribution200ResponseAttributionFirstTouch**](GetCampaignAttribution200ResponseAttributionFirstTouch.md) |  | [optional] 

## Example

```python
from mailodds.models.get_campaign_attribution200_response_attribution import GetCampaignAttribution200ResponseAttribution

# TODO update the JSON string below
json = "{}"
# create an instance of GetCampaignAttribution200ResponseAttribution from a JSON string
get_campaign_attribution200_response_attribution_instance = GetCampaignAttribution200ResponseAttribution.from_json(json)
# print the JSON string representation of the object
print(GetCampaignAttribution200ResponseAttribution.to_json())

# convert the object into a dict
get_campaign_attribution200_response_attribution_dict = get_campaign_attribution200_response_attribution_instance.to_dict()
# create an instance of GetCampaignAttribution200ResponseAttribution from a dict
get_campaign_attribution200_response_attribution_from_dict = GetCampaignAttribution200ResponseAttribution.from_dict(get_campaign_attribution200_response_attribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


