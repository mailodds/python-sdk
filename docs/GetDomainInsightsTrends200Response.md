# GetDomainInsightsTrends200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**trends** | **List[object]** |  | [optional] 

## Example

```python
from mailodds.models.get_domain_insights_trends200_response import GetDomainInsightsTrends200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainInsightsTrends200Response from a JSON string
get_domain_insights_trends200_response_instance = GetDomainInsightsTrends200Response.from_json(json)
# print the JSON string representation of the object
print(GetDomainInsightsTrends200Response.to_json())

# convert the object into a dict
get_domain_insights_trends200_response_dict = get_domain_insights_trends200_response_instance.to_dict()
# create an instance of GetDomainInsightsTrends200Response from a dict
get_domain_insights_trends200_response_from_dict = GetDomainInsightsTrends200Response.from_dict(get_domain_insights_trends200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


