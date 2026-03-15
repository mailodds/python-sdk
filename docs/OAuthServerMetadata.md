# OAuthServerMetadata

OAuth 2.0 Authorization Server Metadata (RFC 8414)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** |  | [optional] 
**authorization_endpoint** | **str** |  | [optional] 
**token_endpoint** | **str** |  | [optional] 
**revocation_endpoint** | **str** |  | [optional] 
**introspection_endpoint** | **str** |  | [optional] 
**jwks_uri** | **str** |  | [optional] 
**response_types_supported** | **List[str]** |  | [optional] 
**grant_types_supported** | **List[str]** |  | [optional] 
**token_endpoint_auth_methods_supported** | **List[str]** |  | [optional] 
**scopes_supported** | **List[str]** |  | [optional] 
**code_challenge_methods_supported** | **List[str]** |  | [optional] 
**revocation_endpoint_auth_methods_supported** | **List[str]** |  | [optional] 
**introspection_endpoint_auth_methods_supported** | **List[str]** |  | [optional] 

## Example

```python
from mailodds.models.o_auth_server_metadata import OAuthServerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthServerMetadata from a JSON string
o_auth_server_metadata_instance = OAuthServerMetadata.from_json(json)
# print the JSON string representation of the object
print(OAuthServerMetadata.to_json())

# convert the object into a dict
o_auth_server_metadata_dict = o_auth_server_metadata_instance.to_dict()
# create an instance of OAuthServerMetadata from a dict
o_auth_server_metadata_from_dict = OAuthServerMetadata.from_dict(o_auth_server_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


