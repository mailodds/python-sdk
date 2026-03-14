# GetCampaignFunnel200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** | Unique request identifier | [optional] 
**campaign_id** | **str** |  | [optional] 
**funnel** | [**GetCampaignFunnel200ResponseFunnel**](GetCampaignFunnel200ResponseFunnel.md) |  | [optional] 
**rates** | [**GetCampaignFunnel200ResponseRates**](GetCampaignFunnel200ResponseRates.md) |  | [optional] 

## Example

```python
from mailodds.models.get_campaign_funnel200_response import GetCampaignFunnel200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCampaignFunnel200Response from a JSON string
get_campaign_funnel200_response_instance = GetCampaignFunnel200Response.from_json(json)
# print the JSON string representation of the object
print(GetCampaignFunnel200Response.to_json())

# convert the object into a dict
get_campaign_funnel200_response_dict = get_campaign_funnel200_response_instance.to_dict()
# create an instance of GetCampaignFunnel200Response from a dict
get_campaign_funnel200_response_from_dict = GetCampaignFunnel200Response.from_dict(get_campaign_funnel200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


