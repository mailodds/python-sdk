# GetDomainInsightsFunnel200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**funnel** | **object** |  | [optional] 

## Example

```python
from mailodds.models.get_domain_insights_funnel200_response import GetDomainInsightsFunnel200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainInsightsFunnel200Response from a JSON string
get_domain_insights_funnel200_response_instance = GetDomainInsightsFunnel200Response.from_json(json)
# print the JSON string representation of the object
print(GetDomainInsightsFunnel200Response.to_json())

# convert the object into a dict
get_domain_insights_funnel200_response_dict = get_domain_insights_funnel200_response_instance.to_dict()
# create an instance of GetDomainInsightsFunnel200Response from a dict
get_domain_insights_funnel200_response_from_dict = GetDomainInsightsFunnel200Response.from_dict(get_domain_insights_funnel200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


