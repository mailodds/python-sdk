# AddDmarcDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name to monitor | 

## Example

```python
from mailodds.models.add_dmarc_domain_request import AddDmarcDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDmarcDomainRequest from a JSON string
add_dmarc_domain_request_instance = AddDmarcDomainRequest.from_json(json)
# print the JSON string representation of the object
print(AddDmarcDomainRequest.to_json())

# convert the object into a dict
add_dmarc_domain_request_dict = add_dmarc_domain_request_instance.to_dict()
# create an instance of AddDmarcDomainRequest from a dict
add_dmarc_domain_request_from_dict = AddDmarcDomainRequest.from_dict(add_dmarc_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


