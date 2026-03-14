# GetCampaignFunnel200ResponseRates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_rate** | **float** |  | [optional] 
**open_rate** | **float** |  | [optional] 
**click_rate** | **float** |  | [optional] 
**click_to_open_rate** | **float** |  | [optional] 
**bounce_rate** | **float** |  | [optional] 
**unsubscribe_rate** | **float** |  | [optional] 
**complaint_rate** | **float** |  | [optional] 

## Example

```python
from mailodds.models.get_campaign_funnel200_response_rates import GetCampaignFunnel200ResponseRates

# TODO update the JSON string below
json = "{}"
# create an instance of GetCampaignFunnel200ResponseRates from a JSON string
get_campaign_funnel200_response_rates_instance = GetCampaignFunnel200ResponseRates.from_json(json)
# print the JSON string representation of the object
print(GetCampaignFunnel200ResponseRates.to_json())

# convert the object into a dict
get_campaign_funnel200_response_rates_dict = get_campaign_funnel200_response_rates_instance.to_dict()
# create an instance of GetCampaignFunnel200ResponseRates from a dict
get_campaign_funnel200_response_rates_from_dict = GetCampaignFunnel200ResponseRates.from_dict(get_campaign_funnel200_response_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


