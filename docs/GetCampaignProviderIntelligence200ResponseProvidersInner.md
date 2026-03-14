# GetCampaignProviderIntelligence200ResponseProvidersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Provider name (e.g. gmail, outlook, yahoo) | [optional] 
**sent** | **int** |  | [optional] 
**delivered** | **int** |  | [optional] 
**bounced** | **int** |  | [optional] 
**opened** | **int** |  | [optional] 
**clicked** | **int** |  | [optional] 
**delivery_rate** | **float** |  | [optional] 
**open_rate** | **float** |  | [optional] 
**click_rate** | **float** |  | [optional] 

## Example

```python
from mailodds.models.get_campaign_provider_intelligence200_response_providers_inner import GetCampaignProviderIntelligence200ResponseProvidersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCampaignProviderIntelligence200ResponseProvidersInner from a JSON string
get_campaign_provider_intelligence200_response_providers_inner_instance = GetCampaignProviderIntelligence200ResponseProvidersInner.from_json(json)
# print the JSON string representation of the object
print(GetCampaignProviderIntelligence200ResponseProvidersInner.to_json())

# convert the object into a dict
get_campaign_provider_intelligence200_response_providers_inner_dict = get_campaign_provider_intelligence200_response_providers_inner_instance.to_dict()
# create an instance of GetCampaignProviderIntelligence200ResponseProvidersInner from a dict
get_campaign_provider_intelligence200_response_providers_inner_from_dict = GetCampaignProviderIntelligence200ResponseProvidersInner.from_dict(get_campaign_provider_intelligence200_response_providers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


