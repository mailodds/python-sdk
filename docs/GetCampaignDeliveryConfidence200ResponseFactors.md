# GetCampaignDeliveryConfidence200ResponseFactors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_quality** | [**GetCampaignDeliveryConfidence200ResponseFactorsListQuality**](GetCampaignDeliveryConfidence200ResponseFactorsListQuality.md) |  | [optional] 
**sender_reputation** | [**GetCampaignDeliveryConfidence200ResponseFactorsSenderReputation**](GetCampaignDeliveryConfidence200ResponseFactorsSenderReputation.md) |  | [optional] 
**domain_auth** | [**GetCampaignDeliveryConfidence200ResponseFactorsDomainAuth**](GetCampaignDeliveryConfidence200ResponseFactorsDomainAuth.md) |  | [optional] 

## Example

```python
from mailodds.models.get_campaign_delivery_confidence200_response_factors import GetCampaignDeliveryConfidence200ResponseFactors

# TODO update the JSON string below
json = "{}"
# create an instance of GetCampaignDeliveryConfidence200ResponseFactors from a JSON string
get_campaign_delivery_confidence200_response_factors_instance = GetCampaignDeliveryConfidence200ResponseFactors.from_json(json)
# print the JSON string representation of the object
print(GetCampaignDeliveryConfidence200ResponseFactors.to_json())

# convert the object into a dict
get_campaign_delivery_confidence200_response_factors_dict = get_campaign_delivery_confidence200_response_factors_instance.to_dict()
# create an instance of GetCampaignDeliveryConfidence200ResponseFactors from a dict
get_campaign_delivery_confidence200_response_factors_from_dict = GetCampaignDeliveryConfidence200ResponseFactors.from_dict(get_campaign_delivery_confidence200_response_factors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


