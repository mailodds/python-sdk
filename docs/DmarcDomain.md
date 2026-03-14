# DmarcDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Domain UUID | [optional] 
**domain** | **str** | Domain name | [optional] 
**reporting_address** | **str** | DMARC aggregate report receiving address | [optional] 
**dns_verified** | **bool** | Whether DNS record has been verified | [optional] 
**dns_verified_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.dmarc_domain import DmarcDomain

# TODO update the JSON string below
json = "{}"
# create an instance of DmarcDomain from a JSON string
dmarc_domain_instance = DmarcDomain.from_json(json)
# print the JSON string representation of the object
print(DmarcDomain.to_json())

# convert the object into a dict
dmarc_domain_dict = dmarc_domain_instance.to_dict()
# create an instance of DmarcDomain from a dict
dmarc_domain_from_dict = DmarcDomain.from_dict(dmarc_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


