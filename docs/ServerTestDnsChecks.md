# ServerTestDnsChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spf** | **bool** |  | [optional] 
**dkim** | **bool** |  | [optional] 
**dmarc** | **bool** |  | [optional] 
**dmarc_policy** | **str** |  | [optional] 

## Example

```python
from mailodds.models.server_test_dns_checks import ServerTestDnsChecks

# TODO update the JSON string below
json = "{}"
# create an instance of ServerTestDnsChecks from a JSON string
server_test_dns_checks_instance = ServerTestDnsChecks.from_json(json)
# print the JSON string representation of the object
print(ServerTestDnsChecks.to_json())

# convert the object into a dict
server_test_dns_checks_dict = server_test_dns_checks_instance.to_dict()
# create an instance of ServerTestDnsChecks from a dict
server_test_dns_checks_from_dict = ServerTestDnsChecks.from_dict(server_test_dns_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


