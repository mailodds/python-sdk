# GetDmarcDomain200ResponseDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Domain UUID | [optional] 
**domain** | **str** | Domain name | [optional] 
**reporting_address** | **str** | DMARC aggregate report receiving address | [optional] 
**dns_verified** | **bool** | Whether DNS record has been verified | [optional] 
**dns_verified_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**summary** | [**GetDmarcDomain200ResponseDomainAllOfSummary**](GetDmarcDomain200ResponseDomainAllOfSummary.md) |  | [optional] 

## Example

```python
from mailodds.models.get_dmarc_domain200_response_domain import GetDmarcDomain200ResponseDomain

# TODO update the JSON string below
json = "{}"
# create an instance of GetDmarcDomain200ResponseDomain from a JSON string
get_dmarc_domain200_response_domain_instance = GetDmarcDomain200ResponseDomain.from_json(json)
# print the JSON string representation of the object
print(GetDmarcDomain200ResponseDomain.to_json())

# convert the object into a dict
get_dmarc_domain200_response_domain_dict = get_dmarc_domain200_response_domain_instance.to_dict()
# create an instance of GetDmarcDomain200ResponseDomain from a dict
get_dmarc_domain200_response_domain_from_dict = GetDmarcDomain200ResponseDomain.from_dict(get_dmarc_domain200_response_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


