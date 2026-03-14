# GetCampaignDeliveryConfidence200ResponseFactorsListQuality


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** |  | [optional] 
**total_recipients** | **int** |  | [optional] 
**validated_pct** | **float** |  | [optional] 
**suppressed_count** | **int** |  | [optional] 

## Example

```python
from mailodds.models.get_campaign_delivery_confidence200_response_factors_list_quality import GetCampaignDeliveryConfidence200ResponseFactorsListQuality

# TODO update the JSON string below
json = "{}"
# create an instance of GetCampaignDeliveryConfidence200ResponseFactorsListQuality from a JSON string
get_campaign_delivery_confidence200_response_factors_list_quality_instance = GetCampaignDeliveryConfidence200ResponseFactorsListQuality.from_json(json)
# print the JSON string representation of the object
print(GetCampaignDeliveryConfidence200ResponseFactorsListQuality.to_json())

# convert the object into a dict
get_campaign_delivery_confidence200_response_factors_list_quality_dict = get_campaign_delivery_confidence200_response_factors_list_quality_instance.to_dict()
# create an instance of GetCampaignDeliveryConfidence200ResponseFactorsListQuality from a dict
get_campaign_delivery_confidence200_response_factors_list_quality_from_dict = GetCampaignDeliveryConfidence200ResponseFactorsListQuality.from_dict(get_campaign_delivery_confidence200_response_factors_list_quality_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


