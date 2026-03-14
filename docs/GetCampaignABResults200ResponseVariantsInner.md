# GetCampaignABResults200ResponseVariantsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**weight** | **int** |  | [optional] 
**sent** | **int** |  | [optional] 
**delivered** | **int** |  | [optional] 
**opened** | **int** |  | [optional] 
**clicked** | **int** |  | [optional] 
**bounced** | **int** |  | [optional] 
**open_rate** | **float** |  | [optional] 
**click_rate** | **float** |  | [optional] 

## Example

```python
from mailodds.models.get_campaign_ab_results200_response_variants_inner import GetCampaignABResults200ResponseVariantsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCampaignABResults200ResponseVariantsInner from a JSON string
get_campaign_ab_results200_response_variants_inner_instance = GetCampaignABResults200ResponseVariantsInner.from_json(json)
# print the JSON string representation of the object
print(GetCampaignABResults200ResponseVariantsInner.to_json())

# convert the object into a dict
get_campaign_ab_results200_response_variants_inner_dict = get_campaign_ab_results200_response_variants_inner_instance.to_dict()
# create an instance of GetCampaignABResults200ResponseVariantsInner from a dict
get_campaign_ab_results200_response_variants_inner_from_dict = GetCampaignABResults200ResponseVariantsInner.from_dict(get_campaign_ab_results200_response_variants_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


