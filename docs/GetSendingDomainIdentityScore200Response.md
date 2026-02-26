# GetSendingDomainIdentityScore200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_score** | [**SendingDomainIdentityScore**](SendingDomainIdentityScore.md) |  | [optional] 

## Example

```python
from mailodds.models.get_sending_domain_identity_score200_response import GetSendingDomainIdentityScore200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSendingDomainIdentityScore200Response from a JSON string
get_sending_domain_identity_score200_response_instance = GetSendingDomainIdentityScore200Response.from_json(json)
# print the JSON string representation of the object
print(GetSendingDomainIdentityScore200Response.to_json())

# convert the object into a dict
get_sending_domain_identity_score200_response_dict = get_sending_domain_identity_score200_response_instance.to_dict()
# create an instance of GetSendingDomainIdentityScore200Response from a dict
get_sending_domain_identity_score200_response_from_dict = GetSendingDomainIdentityScore200Response.from_dict(get_sending_domain_identity_score200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


