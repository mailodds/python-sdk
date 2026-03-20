# Campaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Campaign UUID | 
**account_id** | **int** |  | [optional] 
**name** | **str** | Campaign name | 
**status** | **str** |  | 
**domain_id** | **str** | Sending domain UUID | 
**subject** | **str** |  | [optional] 
**from_address** | **str** | Sender email address | 
**reply_to** | **str** |  | [optional] 
**html_body** | **str** |  | [optional] 
**text_body** | **str** |  | [optional] 
**html_body_dark** | **str** |  | [optional] 
**text_body_dark** | **str** |  | [optional] 
**campaign_type** | **str** |  | [optional] 
**auto_detect_schema** | **bool** |  | [optional] 
**promo_annotations** | **object** |  | [optional] 
**throwaway_policy** | **str** |  | [optional] 
**scheduled_at** | **datetime** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**recipient_count** | **int** |  | [optional] 
**is_ab_test** | **bool** |  | [optional] 
**winning_variant_id** | **str** |  | [optional] 
**ab_test_config** | **object** |  | [optional] 
**error_message** | **str** |  | [optional] 
**stats** | [**CampaignStats**](CampaignStats.md) |  | [optional] 
**open_rate** | **float** |  | [optional] 
**click_rate** | **float** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.campaign import Campaign

# TODO update the JSON string below
json = "{}"
# create an instance of Campaign from a JSON string
campaign_instance = Campaign.from_json(json)
# print the JSON string representation of the object
print(Campaign.to_json())

# convert the object into a dict
campaign_dict = campaign_instance.to_dict()
# create an instance of Campaign from a dict
campaign_from_dict = Campaign.from_dict(campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


