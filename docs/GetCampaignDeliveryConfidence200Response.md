# GetCampaignDeliveryConfidence200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** | Unique request identifier | [optional] 
**campaign_id** | **str** |  | [optional] 
**confidence_score** | **int** | Predicted delivery confidence (0-100) | [optional] 
**factors** | [**GetCampaignDeliveryConfidence200ResponseFactors**](GetCampaignDeliveryConfidence200ResponseFactors.md) |  | [optional] 
**recommendations** | **List[str]** | Actionable recommendations to improve delivery confidence | [optional] 

## Example

```python
from mailodds.models.get_campaign_delivery_confidence200_response import GetCampaignDeliveryConfidence200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCampaignDeliveryConfidence200Response from a JSON string
get_campaign_delivery_confidence200_response_instance = GetCampaignDeliveryConfidence200Response.from_json(json)
# print the JSON string representation of the object
print(GetCampaignDeliveryConfidence200Response.to_json())

# convert the object into a dict
get_campaign_delivery_confidence200_response_dict = get_campaign_delivery_confidence200_response_instance.to_dict()
# create an instance of GetCampaignDeliveryConfidence200Response from a dict
get_campaign_delivery_confidence200_response_from_dict = GetCampaignDeliveryConfidence200Response.from_dict(get_campaign_delivery_confidence200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


