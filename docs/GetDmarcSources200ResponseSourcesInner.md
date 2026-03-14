# GetDmarcSources200ResponseSourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_ip** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**org** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**dkim_pass** | **int** |  | [optional] 
**dkim_fail** | **int** |  | [optional] 
**spf_pass** | **int** |  | [optional] 
**spf_fail** | **int** |  | [optional] 
**disposition** | **str** |  | [optional] 

## Example

```python
from mailodds.models.get_dmarc_sources200_response_sources_inner import GetDmarcSources200ResponseSourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDmarcSources200ResponseSourcesInner from a JSON string
get_dmarc_sources200_response_sources_inner_instance = GetDmarcSources200ResponseSourcesInner.from_json(json)
# print the JSON string representation of the object
print(GetDmarcSources200ResponseSourcesInner.to_json())

# convert the object into a dict
get_dmarc_sources200_response_sources_inner_dict = get_dmarc_sources200_response_sources_inner_instance.to_dict()
# create an instance of GetDmarcSources200ResponseSourcesInner from a dict
get_dmarc_sources200_response_sources_inner_from_dict = GetDmarcSources200ResponseSourcesInner.from_dict(get_dmarc_sources200_response_sources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


