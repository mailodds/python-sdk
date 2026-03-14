# GetCampaignABResults200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** | Unique request identifier | [optional] 
**campaign_id** | **str** |  | [optional] 
**variants** | [**List[GetCampaignABResults200ResponseVariantsInner]**](GetCampaignABResults200ResponseVariantsInner.md) |  | [optional] 
**winner** | [**GetCampaignABResults200ResponseWinner**](GetCampaignABResults200ResponseWinner.md) |  | [optional] 

## Example

```python
from mailodds.models.get_campaign_ab_results200_response import GetCampaignABResults200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCampaignABResults200Response from a JSON string
get_campaign_ab_results200_response_instance = GetCampaignABResults200Response.from_json(json)
# print the JSON string representation of the object
print(GetCampaignABResults200Response.to_json())

# convert the object into a dict
get_campaign_ab_results200_response_dict = get_campaign_ab_results200_response_instance.to_dict()
# create an instance of GetCampaignABResults200Response from a dict
get_campaign_ab_results200_response_from_dict = GetCampaignABResults200Response.from_dict(get_campaign_ab_results200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


