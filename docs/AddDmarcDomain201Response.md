# AddDmarcDomain201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**domain** | [**DmarcDomain**](DmarcDomain.md) |  | [optional] 

## Example

```python
from mailodds.models.add_dmarc_domain201_response import AddDmarcDomain201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddDmarcDomain201Response from a JSON string
add_dmarc_domain201_response_instance = AddDmarcDomain201Response.from_json(json)
# print the JSON string representation of the object
print(AddDmarcDomain201Response.to_json())

# convert the object into a dict
add_dmarc_domain201_response_dict = add_dmarc_domain201_response_instance.to_dict()
# create an instance of AddDmarcDomain201Response from a dict
add_dmarc_domain201_response_from_dict = AddDmarcDomain201Response.from_dict(add_dmarc_domain201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


