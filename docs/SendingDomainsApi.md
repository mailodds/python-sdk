# mailodds.SendingDomainsApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sending_domain**](SendingDomainsApi.md#create_sending_domain) | **POST** /v1/sending-domains | Add a sending domain
[**delete_sending_domain**](SendingDomainsApi.md#delete_sending_domain) | **DELETE** /v1/sending-domains/{domain_id} | Delete a sending domain
[**get_reply_forwarding**](SendingDomainsApi.md#get_reply_forwarding) | **GET** /v1/sending-domains/{domain_id}/reply-forwarding | Get reply forwarding config
[**get_sending_domain**](SendingDomainsApi.md#get_sending_domain) | **GET** /v1/sending-domains/{domain_id} | Get a sending domain
[**get_sending_domain_identity_score**](SendingDomainsApi.md#get_sending_domain_identity_score) | **GET** /v1/sending-domains/{domain_id}/identity-score | Get domain identity score
[**get_sending_stats**](SendingDomainsApi.md#get_sending_stats) | **GET** /v1/sending-stats | Get sending statistics
[**list_sending_domains**](SendingDomainsApi.md#list_sending_domains) | **GET** /v1/sending-domains | List sending domains
[**set_primary_sending_domain**](SendingDomainsApi.md#set_primary_sending_domain) | **POST** /v1/sending-domains/{domain_id}/set-primary | Set primary sending domain
[**update_reply_forwarding**](SendingDomainsApi.md#update_reply_forwarding) | **PATCH** /v1/sending-domains/{domain_id}/reply-forwarding | Update reply forwarding config
[**verify_sending_domain**](SendingDomainsApi.md#verify_sending_domain) | **POST** /v1/sending-domains/{domain_id}/verify | Verify domain DNS records


# **create_sending_domain**
> CreateSendingDomain201Response create_sending_domain(create_sending_domain_request)

Add a sending domain

Register a new sending domain with NS delegation. After adding, configure DNS records and verify.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_sending_domain201_response import CreateSendingDomain201Response
from mailodds.models.create_sending_domain_request import CreateSendingDomainRequest
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.SendingDomainsApi(api_client)
    create_sending_domain_request = mailodds.CreateSendingDomainRequest() # CreateSendingDomainRequest | 

    try:
        # Add a sending domain
        api_response = api_instance.create_sending_domain(create_sending_domain_request)
        print("The response of SendingDomainsApi->create_sending_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendingDomainsApi->create_sending_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sending_domain_request** | [**CreateSendingDomainRequest**](CreateSendingDomainRequest.md)|  | 

### Return type

[**CreateSendingDomain201Response**](CreateSendingDomain201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Domain created |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sending_domain**
> DeletePolicyRule200Response delete_sending_domain(domain_id)

Delete a sending domain

Permanently remove a sending domain from the account.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.delete_policy_rule200_response import DeletePolicyRule200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.SendingDomainsApi(api_client)
    domain_id = 'domain_id_example' # str | 

    try:
        # Delete a sending domain
        api_response = api_instance.delete_sending_domain(domain_id)
        print("The response of SendingDomainsApi->delete_sending_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendingDomainsApi->delete_sending_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 

### Return type

[**DeletePolicyRule200Response**](DeletePolicyRule200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain deleted |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reply_forwarding**
> GetReplyForwarding200Response get_reply_forwarding(domain_id)

Get reply forwarding config

Get the reply forwarding configuration for a sending domain. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_reply_forwarding200_response import GetReplyForwarding200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.SendingDomainsApi(api_client)
    domain_id = 'domain_id_example' # str | Sending domain ID

    try:
        # Get reply forwarding config
        api_response = api_instance.get_reply_forwarding(domain_id)
        print("The response of SendingDomainsApi->get_reply_forwarding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendingDomainsApi->get_reply_forwarding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Sending domain ID | 

### Return type

[**GetReplyForwarding200Response**](GetReplyForwarding200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reply forwarding configuration |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sending_domain**
> CreateSendingDomain201Response get_sending_domain(domain_id)

Get a sending domain

Get details of a specific sending domain including DNS verification status.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_sending_domain201_response import CreateSendingDomain201Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.SendingDomainsApi(api_client)
    domain_id = 'domain_id_example' # str | 

    try:
        # Get a sending domain
        api_response = api_instance.get_sending_domain(domain_id)
        print("The response of SendingDomainsApi->get_sending_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendingDomainsApi->get_sending_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 

### Return type

[**CreateSendingDomain201Response**](CreateSendingDomain201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain details |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sending_domain_identity_score**
> GetSendingDomainIdentityScore200Response get_sending_domain_identity_score(domain_id)

Get domain identity score

Get a composite DNS health score for the sending domain, checking DKIM, SPF, DMARC, MX, and return path configuration.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_sending_domain_identity_score200_response import GetSendingDomainIdentityScore200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.SendingDomainsApi(api_client)
    domain_id = 'domain_id_example' # str | 

    try:
        # Get domain identity score
        api_response = api_instance.get_sending_domain_identity_score(domain_id)
        print("The response of SendingDomainsApi->get_sending_domain_identity_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendingDomainsApi->get_sending_domain_identity_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 

### Return type

[**GetSendingDomainIdentityScore200Response**](GetSendingDomainIdentityScore200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Identity score |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sending_stats**
> GetSendingStats200Response get_sending_stats(period=period, domain_id=domain_id)

Get sending statistics

Get aggregate sending statistics across all domains for the account, including delivery rates, open rates, and click rates.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_sending_stats200_response import GetSendingStats200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.SendingDomainsApi(api_client)
    period = 7d # str | Time period (optional) (default to 7d)
    domain_id = 'domain_id_example' # str | Filter by domain (optional)

    try:
        # Get sending statistics
        api_response = api_instance.get_sending_stats(period=period, domain_id=domain_id)
        print("The response of SendingDomainsApi->get_sending_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendingDomainsApi->get_sending_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| Time period | [optional] [default to 7d]
 **domain_id** | **str**| Filter by domain | [optional] 

### Return type

[**GetSendingStats200Response**](GetSendingStats200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sending statistics |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sending_domains**
> ListSendingDomains200Response list_sending_domains()

List sending domains

List all sending domains for the authenticated account.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.list_sending_domains200_response import ListSendingDomains200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.SendingDomainsApi(api_client)

    try:
        # List sending domains
        api_response = api_instance.list_sending_domains()
        print("The response of SendingDomainsApi->list_sending_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendingDomainsApi->list_sending_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListSendingDomains200Response**](ListSendingDomains200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of sending domains |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_primary_sending_domain**
> CreateSendingDomain201Response set_primary_sending_domain(domain_id)

Set primary sending domain

Designate a domain as the primary/default sending domain. When domain_id is omitted from deliver calls, the primary domain is used automatically.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_sending_domain201_response import CreateSendingDomain201Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.SendingDomainsApi(api_client)
    domain_id = 'domain_id_example' # str | 

    try:
        # Set primary sending domain
        api_response = api_instance.set_primary_sending_domain(domain_id)
        print("The response of SendingDomainsApi->set_primary_sending_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendingDomainsApi->set_primary_sending_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 

### Return type

[**CreateSendingDomain201Response**](CreateSendingDomain201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Primary domain set |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reply_forwarding**
> GetReplyForwarding200Response update_reply_forwarding(domain_id, update_reply_forwarding_request)

Update reply forwarding config

Configure reply forwarding for a sending domain. Set forward_replies_to to null to disable. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_reply_forwarding200_response import GetReplyForwarding200Response
from mailodds.models.update_reply_forwarding_request import UpdateReplyForwardingRequest
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.SendingDomainsApi(api_client)
    domain_id = 'domain_id_example' # str | Sending domain ID
    update_reply_forwarding_request = mailodds.UpdateReplyForwardingRequest() # UpdateReplyForwardingRequest | 

    try:
        # Update reply forwarding config
        api_response = api_instance.update_reply_forwarding(domain_id, update_reply_forwarding_request)
        print("The response of SendingDomainsApi->update_reply_forwarding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendingDomainsApi->update_reply_forwarding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Sending domain ID | 
 **update_reply_forwarding_request** | [**UpdateReplyForwardingRequest**](UpdateReplyForwardingRequest.md)|  | 

### Return type

[**GetReplyForwarding200Response**](GetReplyForwarding200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reply forwarding updated |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**404** | Resource not found |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_sending_domain**
> CreateSendingDomain201Response verify_sending_domain(domain_id)

Verify domain DNS records

Check and verify all DNS records (DKIM, SPF, DMARC, MX, return path) for the sending domain.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_sending_domain201_response import CreateSendingDomain201Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.SendingDomainsApi(api_client)
    domain_id = 'domain_id_example' # str | 

    try:
        # Verify domain DNS records
        api_response = api_instance.verify_sending_domain(domain_id)
        print("The response of SendingDomainsApi->verify_sending_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendingDomainsApi->verify_sending_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 

### Return type

[**CreateSendingDomain201Response**](CreateSendingDomain201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Verification result |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

