# mailodds.DomainInsightsApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_domain_hook_effectiveness**](DomainInsightsApi.md#get_domain_hook_effectiveness) | **GET** /v1/sending-domains/{domain_id}/insights/hook-effectiveness | Get hook effectiveness metrics
[**get_domain_insights_funnel**](DomainInsightsApi.md#get_domain_insights_funnel) | **GET** /v1/sending-domains/{domain_id}/insights/funnel | Get domain engagement funnel
[**get_domain_insights_trends**](DomainInsightsApi.md#get_domain_insights_trends) | **GET** /v1/sending-domains/{domain_id}/insights/trends | Get domain engagement trends


# **get_domain_hook_effectiveness**
> GetDomainHookEffectiveness200Response get_domain_hook_effectiveness(domain_id, days=days)

Get hook effectiveness metrics

Get webhook delivery effectiveness metrics for a sending domain. Requires Pro+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_domain_hook_effectiveness200_response import GetDomainHookEffectiveness200Response
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
    api_instance = mailodds.DomainInsightsApi(api_client)
    domain_id = 'domain_id_example' # str | Sending domain ID
    days = 30 # int | Lookback period in days (optional) (default to 30)

    try:
        # Get hook effectiveness metrics
        api_response = api_instance.get_domain_hook_effectiveness(domain_id, days=days)
        print("The response of DomainInsightsApi->get_domain_hook_effectiveness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainInsightsApi->get_domain_hook_effectiveness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Sending domain ID | 
 **days** | **int**| Lookback period in days | [optional] [default to 30]

### Return type

[**GetDomainHookEffectiveness200Response**](GetDomainHookEffectiveness200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hook effectiveness metrics |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_insights_funnel**
> GetDomainInsightsFunnel200Response get_domain_insights_funnel(domain_id, days=days)

Get domain engagement funnel

Get engagement funnel for a sending domain (sent > delivered > opened > clicked > converted). Requires Pro+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_domain_insights_funnel200_response import GetDomainInsightsFunnel200Response
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
    api_instance = mailodds.DomainInsightsApi(api_client)
    domain_id = 'domain_id_example' # str | Sending domain ID
    days = 30 # int | Lookback period in days (optional) (default to 30)

    try:
        # Get domain engagement funnel
        api_response = api_instance.get_domain_insights_funnel(domain_id, days=days)
        print("The response of DomainInsightsApi->get_domain_insights_funnel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainInsightsApi->get_domain_insights_funnel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Sending domain ID | 
 **days** | **int**| Lookback period in days | [optional] [default to 30]

### Return type

[**GetDomainInsightsFunnel200Response**](GetDomainInsightsFunnel200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Engagement funnel data |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_insights_trends**
> GetDomainInsightsTrends200Response get_domain_insights_trends(domain_id, days=days)

Get domain engagement trends

Get daily engagement trend data for a sending domain. Requires Pro+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_domain_insights_trends200_response import GetDomainInsightsTrends200Response
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
    api_instance = mailodds.DomainInsightsApi(api_client)
    domain_id = 'domain_id_example' # str | Sending domain ID
    days = 30 # int | Lookback period in days (optional) (default to 30)

    try:
        # Get domain engagement trends
        api_response = api_instance.get_domain_insights_trends(domain_id, days=days)
        print("The response of DomainInsightsApi->get_domain_insights_trends:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainInsightsApi->get_domain_insights_trends: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Sending domain ID | 
 **days** | **int**| Lookback period in days | [optional] [default to 30]

### Return type

[**GetDomainInsightsTrends200Response**](GetDomainInsightsTrends200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Engagement trend data |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

