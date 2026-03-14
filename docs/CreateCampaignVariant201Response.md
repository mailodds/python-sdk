# CreateCampaignVariant201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** | Unique request identifier | [optional] 
**variant** | [**CampaignVariant**](CampaignVariant.md) |  | [optional] 

## Example

```python
from mailodds.models.create_campaign_variant201_response import CreateCampaignVariant201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCampaignVariant201Response from a JSON string
create_campaign_variant201_response_instance = CreateCampaignVariant201Response.from_json(json)
# print the JSON string representation of the object
print(CreateCampaignVariant201Response.to_json())

# convert the object into a dict
create_campaign_variant201_response_dict = create_campaign_variant201_response_instance.to_dict()
# create an instance of CreateCampaignVariant201Response from a dict
create_campaign_variant201_response_from_dict = CreateCampaignVariant201Response.from_dict(create_campaign_variant201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


