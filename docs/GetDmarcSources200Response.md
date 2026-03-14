# GetDmarcSources200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**sources** | [**List[GetDmarcSources200ResponseSourcesInner]**](GetDmarcSources200ResponseSourcesInner.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from mailodds.models.get_dmarc_sources200_response import GetDmarcSources200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDmarcSources200Response from a JSON string
get_dmarc_sources200_response_instance = GetDmarcSources200Response.from_json(json)
# print the JSON string representation of the object
print(GetDmarcSources200Response.to_json())

# convert the object into a dict
get_dmarc_sources200_response_dict = get_dmarc_sources200_response_instance.to_dict()
# create an instance of GetDmarcSources200Response from a dict
get_dmarc_sources200_response_from_dict = GetDmarcSources200Response.from_dict(get_dmarc_sources200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


