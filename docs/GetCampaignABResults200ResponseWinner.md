# GetCampaignABResults200ResponseWinner

Winning variant, or null if no statistical winner yet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant_id** | **str** |  | [optional] 
**metric** | **str** | Metric used to determine winner (open_rate or click_rate) | [optional] 
**confidence** | **float** | Statistical confidence level (0-1) | [optional] 

## Example

```python
from mailodds.models.get_campaign_ab_results200_response_winner import GetCampaignABResults200ResponseWinner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCampaignABResults200ResponseWinner from a JSON string
get_campaign_ab_results200_response_winner_instance = GetCampaignABResults200ResponseWinner.from_json(json)
# print the JSON string representation of the object
print(GetCampaignABResults200ResponseWinner.to_json())

# convert the object into a dict
get_campaign_ab_results200_response_winner_dict = get_campaign_ab_results200_response_winner_instance.to_dict()
# create an instance of GetCampaignABResults200ResponseWinner from a dict
get_campaign_ab_results200_response_winner_from_dict = GetCampaignABResults200ResponseWinner.from_dict(get_campaign_ab_results200_response_winner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


