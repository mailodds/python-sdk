# GetEngagementScore200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**last_engaged_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.get_engagement_score200_response import GetEngagementScore200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEngagementScore200Response from a JSON string
get_engagement_score200_response_instance = GetEngagementScore200Response.from_json(json)
# print the JSON string representation of the object
print(GetEngagementScore200Response.to_json())

# convert the object into a dict
get_engagement_score200_response_dict = get_engagement_score200_response_instance.to_dict()
# create an instance of GetEngagementScore200Response from a dict
get_engagement_score200_response_from_dict = GetEngagementScore200Response.from_dict(get_engagement_score200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


