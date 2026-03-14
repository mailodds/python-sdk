# CampaignVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Variant UUID | 
**campaign_id** | **str** |  | 
**name** | **str** | Variant name (e.g., \&quot;Variant A\&quot;) | 
**subject** | **str** |  | 
**html** | **str** | HTML email body | [optional] 
**text** | **str** | Plain text email body | [optional] 
**weight** | **int** | Traffic weight percentage (all variant weights must sum to 100) | 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.campaign_variant import CampaignVariant

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignVariant from a JSON string
campaign_variant_instance = CampaignVariant.from_json(json)
# print the JSON string representation of the object
print(CampaignVariant.to_json())

# convert the object into a dict
campaign_variant_dict = campaign_variant_instance.to_dict()
# create an instance of CampaignVariant from a dict
campaign_variant_from_dict = CampaignVariant.from_dict(campaign_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


