# SendingDomainDnsRecordsNs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Record type (NS) | [optional] 
**host** | **str** | NS record host (mo.yourdomain.com) | [optional] 
**targets** | **List[str]** | NS target servers | [optional] 
**status** | **str** | Verification status | [optional] 
**verified_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.sending_domain_dns_records_ns import SendingDomainDnsRecordsNs

# TODO update the JSON string below
json = "{}"
# create an instance of SendingDomainDnsRecordsNs from a JSON string
sending_domain_dns_records_ns_instance = SendingDomainDnsRecordsNs.from_json(json)
# print the JSON string representation of the object
print(SendingDomainDnsRecordsNs.to_json())

# convert the object into a dict
sending_domain_dns_records_ns_dict = sending_domain_dns_records_ns_instance.to_dict()
# create an instance of SendingDomainDnsRecordsNs from a dict
sending_domain_dns_records_ns_from_dict = SendingDomainDnsRecordsNs.from_dict(sending_domain_dns_records_ns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


