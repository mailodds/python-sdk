# mailodds.DMARCMonitoringApi

All URIs are relative to *https://api.mailodds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dmarc_domain**](DMARCMonitoringApi.md#add_dmarc_domain) | **POST** /v1/dmarc-domains | Add DMARC domain
[**delete_dmarc_domain**](DMARCMonitoringApi.md#delete_dmarc_domain) | **DELETE** /v1/dmarc-domains/{domain_id} | Delete a DMARC domain
[**get_dmarc_domain**](DMARCMonitoringApi.md#get_dmarc_domain) | **GET** /v1/dmarc-domains/{domain_id} | Get DMARC domain
[**get_dmarc_recommendation**](DMARCMonitoringApi.md#get_dmarc_recommendation) | **GET** /v1/dmarc-domains/{domain_id}/recommendation | Get DMARC policy recommendation
[**get_dmarc_sources**](DMARCMonitoringApi.md#get_dmarc_sources) | **GET** /v1/dmarc-domains/{domain_id}/sources | Get DMARC sending sources
[**get_dmarc_trend**](DMARCMonitoringApi.md#get_dmarc_trend) | **GET** /v1/dmarc-domains/{domain_id}/trend | Get DMARC trend
[**list_dmarc_domains**](DMARCMonitoringApi.md#list_dmarc_domains) | **GET** /v1/dmarc-domains | List DMARC domains
[**verify_dmarc_domain**](DMARCMonitoringApi.md#verify_dmarc_domain) | **POST** /v1/dmarc-domains/{domain_id}/verify | Verify DMARC DNS records


# **add_dmarc_domain**
> AddDmarcDomain201Response add_dmarc_domain(add_dmarc_domain_request)

Add DMARC domain

Add a domain for DMARC monitoring. A unique reporting address is generated for receiving aggregate DMARC reports.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.add_dmarc_domain201_response import AddDmarcDomain201Response
from mailodds.models.add_dmarc_domain_request import AddDmarcDomainRequest
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.DMARCMonitoringApi(api_client)
    add_dmarc_domain_request = mailodds.AddDmarcDomainRequest() # AddDmarcDomainRequest | 

    try:
        # Add DMARC domain
        api_response = api_instance.add_dmarc_domain(add_dmarc_domain_request)
        print("The response of DMARCMonitoringApi->add_dmarc_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DMARCMonitoringApi->add_dmarc_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_dmarc_domain_request** | [**AddDmarcDomainRequest**](AddDmarcDomainRequest.md)|  | 

### Return type

[**AddDmarcDomain201Response**](AddDmarcDomain201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Domain added |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dmarc_domain**
> DeletePolicyRule200Response delete_dmarc_domain(domain_id)

Delete a DMARC domain

Delete a DMARC domain and all its associated reports.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.delete_policy_rule200_response import DeletePolicyRule200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.DMARCMonitoringApi(api_client)
    domain_id = 'domain_id_example' # str | DMARC domain UUID

    try:
        # Delete a DMARC domain
        api_response = api_instance.delete_dmarc_domain(domain_id)
        print("The response of DMARCMonitoringApi->delete_dmarc_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DMARCMonitoringApi->delete_dmarc_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| DMARC domain UUID | 

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

# **get_dmarc_domain**
> GetDmarcDomain200Response get_dmarc_domain(domain_id, days=days)

Get DMARC domain

Get a single DMARC domain with summary statistics including pass/fail rates.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_dmarc_domain200_response import GetDmarcDomain200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.DMARCMonitoringApi(api_client)
    domain_id = 'domain_id_example' # str | DMARC domain UUID
    days = 30 # int | Number of days for summary stats (optional) (default to 30)

    try:
        # Get DMARC domain
        api_response = api_instance.get_dmarc_domain(domain_id, days=days)
        print("The response of DMARCMonitoringApi->get_dmarc_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DMARCMonitoringApi->get_dmarc_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| DMARC domain UUID | 
 **days** | **int**| Number of days for summary stats | [optional] [default to 30]

### Return type

[**GetDmarcDomain200Response**](GetDmarcDomain200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain with summary stats |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dmarc_recommendation**
> GetDmarcRecommendation200Response get_dmarc_recommendation(domain_id)

Get DMARC policy recommendation

Get a recommendation for upgrading the domain's DMARC policy based on alignment data.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_dmarc_recommendation200_response import GetDmarcRecommendation200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.DMARCMonitoringApi(api_client)
    domain_id = 'domain_id_example' # str | DMARC domain UUID

    try:
        # Get DMARC policy recommendation
        api_response = api_instance.get_dmarc_recommendation(domain_id)
        print("The response of DMARCMonitoringApi->get_dmarc_recommendation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DMARCMonitoringApi->get_dmarc_recommendation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| DMARC domain UUID | 

### Return type

[**GetDmarcRecommendation200Response**](GetDmarcRecommendation200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Policy recommendation |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dmarc_sources**
> GetDmarcSources200Response get_dmarc_sources(domain_id, days=days, page=page, per_page=per_page)

Get DMARC sending sources

Get sending IPs that have sent email for this domain with their DKIM/SPF alignment status.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_dmarc_sources200_response import GetDmarcSources200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.DMARCMonitoringApi(api_client)
    domain_id = 'domain_id_example' # str | DMARC domain UUID
    days = 30 # int | Number of days to look back (optional) (default to 30)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)

    try:
        # Get DMARC sending sources
        api_response = api_instance.get_dmarc_sources(domain_id, days=days, page=page, per_page=per_page)
        print("The response of DMARCMonitoringApi->get_dmarc_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DMARCMonitoringApi->get_dmarc_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| DMARC domain UUID | 
 **days** | **int**| Number of days to look back | [optional] [default to 30]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]

### Return type

[**GetDmarcSources200Response**](GetDmarcSources200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sending sources with alignment status |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dmarc_trend**
> GetDmarcTrend200Response get_dmarc_trend(domain_id, days=days)

Get DMARC trend

Get daily pass/fail trend data for DMARC authentication over the specified period.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_dmarc_trend200_response import GetDmarcTrend200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.DMARCMonitoringApi(api_client)
    domain_id = 'domain_id_example' # str | DMARC domain UUID
    days = 30 # int | Number of days of trend data (optional) (default to 30)

    try:
        # Get DMARC trend
        api_response = api_instance.get_dmarc_trend(domain_id, days=days)
        print("The response of DMARCMonitoringApi->get_dmarc_trend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DMARCMonitoringApi->get_dmarc_trend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| DMARC domain UUID | 
 **days** | **int**| Number of days of trend data | [optional] [default to 30]

### Return type

[**GetDmarcTrend200Response**](GetDmarcTrend200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Daily trend data |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dmarc_domains**
> ListDmarcDomains200Response list_dmarc_domains()

List DMARC domains

List all domains being monitored for DMARC compliance.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.list_dmarc_domains200_response import ListDmarcDomains200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.DMARCMonitoringApi(api_client)

    try:
        # List DMARC domains
        api_response = api_instance.list_dmarc_domains()
        print("The response of DMARCMonitoringApi->list_dmarc_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DMARCMonitoringApi->list_dmarc_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDmarcDomains200Response**](ListDmarcDomains200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of monitored domains |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_dmarc_domain**
> AddDmarcDomain201Response verify_dmarc_domain(domain_id)

Verify DMARC DNS records

Check that the domain has the correct DMARC TXT record pointing to the MailOdds reporting address.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.add_dmarc_domain201_response import AddDmarcDomain201Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.DMARCMonitoringApi(api_client)
    domain_id = 'domain_id_example' # str | DMARC domain UUID

    try:
        # Verify DMARC DNS records
        api_response = api_instance.verify_dmarc_domain(domain_id)
        print("The response of DMARCMonitoringApi->verify_dmarc_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DMARCMonitoringApi->verify_dmarc_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| DMARC domain UUID | 

### Return type

[**AddDmarcDomain201Response**](AddDmarcDomain201Response.md)

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

