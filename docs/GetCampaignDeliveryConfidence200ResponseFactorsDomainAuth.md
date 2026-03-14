# GetCampaignDeliveryConfidence200ResponseFactorsDomainAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** |  | [optional] 
**dkim** | **bool** |  | [optional] 
**spf** | **bool** |  | [optional] 
**dmarc** | **bool** |  | [optional] 

## Example

```python
from mailodds.models.get_campaign_delivery_confidence200_response_factors_domain_auth import GetCampaignDeliveryConfidence200ResponseFactorsDomainAuth

# TODO update the JSON string below
json = "{}"
# create an instance of GetCampaignDeliveryConfidence200ResponseFactorsDomainAuth from a JSON string
get_campaign_delivery_confidence200_response_factors_domain_auth_instance = GetCampaignDeliveryConfidence200ResponseFactorsDomainAuth.from_json(json)
# print the JSON string representation of the object
print(GetCampaignDeliveryConfidence200ResponseFactorsDomainAuth.to_json())

# convert the object into a dict
get_campaign_delivery_confidence200_response_factors_domain_auth_dict = get_campaign_delivery_confidence200_response_factors_domain_auth_instance.to_dict()
# create an instance of GetCampaignDeliveryConfidence200ResponseFactorsDomainAuth from a dict
get_campaign_delivery_confidence200_response_factors_domain_auth_from_dict = GetCampaignDeliveryConfidence200ResponseFactorsDomainAuth.from_dict(get_campaign_delivery_confidence200_response_factors_domain_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


