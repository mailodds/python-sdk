# CreateCampaignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Campaign name | 
**list_id** | **str** | Target subscriber list UUID | 
**domain_id** | **str** | Sending domain UUID | 
**from_email** | **str** | Sender email address (must match the sending domain) | 
**from_name** | **str** | Sender display name | [optional] 
**reply_to** | **str** | Reply-to address | [optional] 
**tags** | **List[str]** | Tags for categorization | [optional] 

## Example

```python
from mailodds.models.create_campaign_request import CreateCampaignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCampaignRequest from a JSON string
create_campaign_request_instance = CreateCampaignRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCampaignRequest.to_json())

# convert the object into a dict
create_campaign_request_dict = create_campaign_request_instance.to_dict()
# create an instance of CreateCampaignRequest from a dict
create_campaign_request_from_dict = CreateCampaignRequest.from_dict(create_campaign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


