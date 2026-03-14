# GetCampaignProviderIntelligence200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**campaign_id** | **str** |  | [optional] 
**providers** | [**List[GetCampaignProviderIntelligence200ResponseProvidersInner]**](GetCampaignProviderIntelligence200ResponseProvidersInner.md) |  | [optional] 

## Example

```python
from mailodds.models.get_campaign_provider_intelligence200_response import GetCampaignProviderIntelligence200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCampaignProviderIntelligence200Response from a JSON string
get_campaign_provider_intelligence200_response_instance = GetCampaignProviderIntelligence200Response.from_json(json)
# print the JSON string representation of the object
print(GetCampaignProviderIntelligence200Response.to_json())

# convert the object into a dict
get_campaign_provider_intelligence200_response_dict = get_campaign_provider_intelligence200_response_instance.to_dict()
# create an instance of GetCampaignProviderIntelligence200Response from a dict
get_campaign_provider_intelligence200_response_from_dict = GetCampaignProviderIntelligence200Response.from_dict(get_campaign_provider_intelligence200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


