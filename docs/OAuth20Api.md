# mailodds.OAuth20Api

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](OAuth20Api.md#create_token) | **POST** /oauth/token | Create token
[**get_jwks**](OAuth20Api.md#get_jwks) | **GET** /.well-known/jwks.json | Get JSON Web Key Set
[**introspect_token**](OAuth20Api.md#introspect_token) | **POST** /oauth/introspect | Introspect token
[**oauth_server_metadata**](OAuth20Api.md#oauth_server_metadata) | **GET** /.well-known/oauth-authorization-server | OAuth server metadata
[**revoke_token**](OAuth20Api.md#revoke_token) | **POST** /oauth/revoke | Revoke token


# **create_token**
> CreateToken200Response create_token(grant_type, code=code, redirect_uri=redirect_uri, client_id=client_id, client_secret=client_secret, refresh_token=refresh_token, scope=scope, code_verifier=code_verifier)

Create token

Exchange an authorization code, client credentials, or refresh token for access and refresh tokens. Authenticate via client_secret_post or client_secret_basic.

### Example


```python
import mailodds
from mailodds.models.create_token200_response import CreateToken200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)


# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.OAuth20Api(api_client)
    grant_type = 'grant_type_example' # str | 
    code = 'code_example' # str | Authorization code (for authorization_code grant) (optional)
    redirect_uri = 'redirect_uri_example' # str | Must match the original redirect_uri (optional)
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)
    refresh_token = 'refresh_token_example' # str | Refresh token (for refresh_token grant) (optional)
    scope = 'scope_example' # str | Space-separated scopes (optional)
    code_verifier = 'code_verifier_example' # str | PKCE code verifier (optional)

    try:
        # Create token
        api_response = api_instance.create_token(grant_type, code=code, redirect_uri=redirect_uri, client_id=client_id, client_secret=client_secret, refresh_token=refresh_token, scope=scope, code_verifier=code_verifier)
        print("The response of OAuth20Api->create_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth20Api->create_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  | 
 **code** | **str**| Authorization code (for authorization_code grant) | [optional] 
 **redirect_uri** | **str**| Must match the original redirect_uri | [optional] 
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 
 **refresh_token** | **str**| Refresh token (for refresh_token grant) | [optional] 
 **scope** | **str**| Space-separated scopes | [optional] 
 **code_verifier** | **str**| PKCE code verifier | [optional] 

### Return type

[**CreateToken200Response**](CreateToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token response |  -  |
**400** | Invalid request or grant |  -  |
**401** | Invalid client credentials |  -  |
**429** | Rate limited (20 req/min per client) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jwks**
> JwksResponse get_jwks()

Get JSON Web Key Set

Public key set for verifying JWT access tokens issued by this server.

### Example


```python
import mailodds
from mailodds.models.jwks_response import JwksResponse
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)


# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.OAuth20Api(api_client)

    try:
        # Get JSON Web Key Set
        api_response = api_instance.get_jwks()
        print("The response of OAuth20Api->get_jwks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth20Api->get_jwks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JwksResponse**](JwksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JWKS response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **introspect_token**
> IntrospectToken200Response introspect_token(token, token_type_hint=token_type_hint, client_id=client_id, client_secret=client_secret)

Introspect token

Introspect a token to determine its active state and metadata (RFC 7662). Requires client authentication.

### Example


```python
import mailodds
from mailodds.models.introspect_token200_response import IntrospectToken200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)


# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.OAuth20Api(api_client)
    token = 'token_example' # str | Token to introspect
    token_type_hint = 'token_type_hint_example' # str |  (optional)
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Introspect token
        api_response = api_instance.introspect_token(token, token_type_hint=token_type_hint, client_id=client_id, client_secret=client_secret)
        print("The response of OAuth20Api->introspect_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth20Api->introspect_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Token to introspect | 
 **token_type_hint** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**IntrospectToken200Response**](IntrospectToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Introspection result |  -  |
**401** | Invalid client credentials |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_server_metadata**
> OAuthServerMetadata oauth_server_metadata()

OAuth server metadata

OAuth 2.0 Authorization Server Metadata (RFC 8414). Returns server configuration including supported grant types, scopes, and endpoints.

### Example


```python
import mailodds
from mailodds.models.o_auth_server_metadata import OAuthServerMetadata
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)


# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.OAuth20Api(api_client)

    try:
        # OAuth server metadata
        api_response = api_instance.oauth_server_metadata()
        print("The response of OAuth20Api->oauth_server_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth20Api->oauth_server_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OAuthServerMetadata**](OAuthServerMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_token**
> revoke_token(token, token_type_hint=token_type_hint, client_id=client_id, client_secret=client_secret)

Revoke token

Revoke an access or refresh token (RFC 7009). Requires client authentication. Always returns 200 per spec to prevent token scanning.

### Example


```python
import mailodds
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)


# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.OAuth20Api(api_client)
    token = 'token_example' # str | Token to revoke
    token_type_hint = 'token_type_hint_example' # str |  (optional)
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Revoke token
        api_instance.revoke_token(token, token_type_hint=token_type_hint, client_id=client_id, client_secret=client_secret)
    except Exception as e:
        print("Exception when calling OAuth20Api->revoke_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Token to revoke | 
 **token_type_hint** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token revoked (or not found, per RFC 7009) |  -  |
**401** | Invalid client credentials |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

