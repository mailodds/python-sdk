# OAuthClientRegistration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Issued client identifier | 
**client_name** | **str** | Human-readable client name | 
**redirect_uris** | **List[str]** | Registered redirect URIs | 
**grant_types** | **List[str]** | Allowed grant types | 
**response_types** | **List[str]** | Allowed response types | 
**token_endpoint_auth_method** | **str** | Token endpoint auth method | 
**scope** | **str** | Allowed scope | [optional] 
**client_id_issued_at** | **int** | Unix timestamp of client registration | 
**client_secret** | **str** | Client secret (only for confidential clients, shown once) | [optional] 
**client_secret_expires_at** | **int** | Secret expiry (0 &#x3D; never) | [optional] 

## Example

```python
from mailodds.models.o_auth_client_registration import OAuthClientRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthClientRegistration from a JSON string
o_auth_client_registration_instance = OAuthClientRegistration.from_json(json)
# print the JSON string representation of the object
print(OAuthClientRegistration.to_json())

# convert the object into a dict
o_auth_client_registration_dict = o_auth_client_registration_instance.to_dict()
# create an instance of OAuthClientRegistration from a dict
o_auth_client_registration_from_dict = OAuthClientRegistration.from_dict(o_auth_client_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


