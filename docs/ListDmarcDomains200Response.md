# ListDmarcDomains200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**domains** | [**List[DmarcDomain]**](DmarcDomain.md) |  | [optional] 

## Example

```python
from mailodds.models.list_dmarc_domains200_response import ListDmarcDomains200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDmarcDomains200Response from a JSON string
list_dmarc_domains200_response_instance = ListDmarcDomains200Response.from_json(json)
# print the JSON string representation of the object
print(ListDmarcDomains200Response.to_json())

# convert the object into a dict
list_dmarc_domains200_response_dict = list_dmarc_domains200_response_instance.to_dict()
# create an instance of ListDmarcDomains200Response from a dict
list_dmarc_domains200_response_from_dict = ListDmarcDomains200Response.from_dict(list_dmarc_domains200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


