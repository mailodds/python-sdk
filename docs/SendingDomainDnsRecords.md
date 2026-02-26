# SendingDomainDnsRecords

DNS records for domain verification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ns** | [**SendingDomainDnsRecordsNs**](SendingDomainDnsRecordsNs.md) |  | [optional] 

## Example

```python
from mailodds.models.sending_domain_dns_records import SendingDomainDnsRecords

# TODO update the JSON string below
json = "{}"
# create an instance of SendingDomainDnsRecords from a JSON string
sending_domain_dns_records_instance = SendingDomainDnsRecords.from_json(json)
# print the JSON string representation of the object
print(SendingDomainDnsRecords.to_json())

# convert the object into a dict
sending_domain_dns_records_dict = sending_domain_dns_records_instance.to_dict()
# create an instance of SendingDomainDnsRecords from a dict
sending_domain_dns_records_from_dict = SendingDomainDnsRecords.from_dict(sending_domain_dns_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


