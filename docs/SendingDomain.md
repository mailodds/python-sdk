# SendingDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Domain UUID | [optional] 
**domain** | **str** | Domain name | [optional] 
**domain_type** | **str** | Domain type (ns_delegated) | [optional] 
**status** | **str** | Domain verification status | [optional] 
**dkim_selector** | **str** | DKIM selector (e.g. mo1) | [optional] 
**dns_records** | [**SendingDomainDnsRecords**](SendingDomainDnsRecords.md) |  | [optional] 
**bimi_svg_url** | **str** | BIMI SVG logo URL | [optional] 
**bimi_vmc_url** | **str** | BIMI VMC certificate URL | [optional] 
**bimi_enabled** | **bool** | Whether BIMI is enabled | [optional] 
**forward_replies_to** | **str** | Reply forwarding address | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.sending_domain import SendingDomain

# TODO update the JSON string below
json = "{}"
# create an instance of SendingDomain from a JSON string
sending_domain_instance = SendingDomain.from_json(json)
# print the JSON string representation of the object
print(SendingDomain.to_json())

# convert the object into a dict
sending_domain_dict = sending_domain_instance.to_dict()
# create an instance of SendingDomain from a dict
sending_domain_from_dict = SendingDomain.from_dict(sending_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


