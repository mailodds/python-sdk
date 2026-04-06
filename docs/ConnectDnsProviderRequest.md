# ConnectDnsProviderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | DNS provider | 
**api_token** | **str** | API token with Zone &gt; DNS &gt; Edit permission | 

## Example

```python
from mailodds.models.connect_dns_provider_request import ConnectDnsProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectDnsProviderRequest from a JSON string
connect_dns_provider_request_instance = ConnectDnsProviderRequest.from_json(json)
# print the JSON string representation of the object
print(ConnectDnsProviderRequest.to_json())

# convert the object into a dict
connect_dns_provider_request_dict = connect_dns_provider_request_instance.to_dict()
# create an instance of ConnectDnsProviderRequest from a dict
connect_dns_provider_request_from_dict = ConnectDnsProviderRequest.from_dict(connect_dns_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


