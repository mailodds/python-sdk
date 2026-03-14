# ListCampaigns200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** | Unique request identifier | [optional] 
**campaigns** | [**List[Campaign]**](Campaign.md) |  | [optional] 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 

## Example

```python
from mailodds.models.list_campaigns200_response import ListCampaigns200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListCampaigns200Response from a JSON string
list_campaigns200_response_instance = ListCampaigns200Response.from_json(json)
# print the JSON string representation of the object
print(ListCampaigns200Response.to_json())

# convert the object into a dict
list_campaigns200_response_dict = list_campaigns200_response_instance.to_dict()
# create an instance of ListCampaigns200Response from a dict
list_campaigns200_response_from_dict = ListCampaigns200Response.from_dict(list_campaigns200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


