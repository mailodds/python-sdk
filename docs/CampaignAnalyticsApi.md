# mailodds.CampaignAnalyticsApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_campaign_ab_results**](CampaignAnalyticsApi.md#get_campaign_ab_results) | **GET** /v1/campaigns/{campaign_id}/ab-results | Get A/B test results
[**get_campaign_attribution**](CampaignAnalyticsApi.md#get_campaign_attribution) | **GET** /v1/campaigns/{campaign_id}/conversions/attribution | Get campaign attribution
[**get_campaign_delivery_confidence**](CampaignAnalyticsApi.md#get_campaign_delivery_confidence) | **GET** /v1/campaigns/{campaign_id}/delivery-confidence | Get pre-send delivery confidence
[**get_campaign_funnel**](CampaignAnalyticsApi.md#get_campaign_funnel) | **GET** /v1/campaigns/{campaign_id}/funnel | Get campaign funnel
[**get_campaign_provider_intelligence**](CampaignAnalyticsApi.md#get_campaign_provider_intelligence) | **GET** /v1/campaigns/{campaign_id}/provider-intelligence | Get provider intelligence


# **get_campaign_ab_results**
> GetCampaignABResults200Response get_campaign_ab_results(campaign_id)

Get A/B test results

Get per-variant performance metrics for an A/B test campaign including open rate, click rate, and statistical confidence.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_campaign_ab_results200_response import GetCampaignABResults200Response
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
    api_instance = mailodds.CampaignAnalyticsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Campaign UUID

    try:
        # Get A/B test results
        api_response = api_instance.get_campaign_ab_results(campaign_id)
        print("The response of CampaignAnalyticsApi->get_campaign_ab_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignAnalyticsApi->get_campaign_ab_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign UUID | 

### Return type

[**GetCampaignABResults200Response**](GetCampaignABResults200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A/B test results |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_attribution**
> GetCampaignAttribution200Response get_campaign_attribution(campaign_id)

Get campaign attribution

Get first-touch and last-touch attribution comparison for campaign conversions.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_campaign_attribution200_response import GetCampaignAttribution200Response
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
    api_instance = mailodds.CampaignAnalyticsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Campaign UUID

    try:
        # Get campaign attribution
        api_response = api_instance.get_campaign_attribution(campaign_id)
        print("The response of CampaignAnalyticsApi->get_campaign_attribution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignAnalyticsApi->get_campaign_attribution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign UUID | 

### Return type

[**GetCampaignAttribution200Response**](GetCampaignAttribution200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attribution data |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_delivery_confidence**
> GetCampaignDeliveryConfidence200Response get_campaign_delivery_confidence(campaign_id)

Get pre-send delivery confidence

Get a predicted delivery confidence score before sending a campaign. Evaluates list quality, sender reputation, and domain authentication.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_campaign_delivery_confidence200_response import GetCampaignDeliveryConfidence200Response
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
    api_instance = mailodds.CampaignAnalyticsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Campaign UUID

    try:
        # Get pre-send delivery confidence
        api_response = api_instance.get_campaign_delivery_confidence(campaign_id)
        print("The response of CampaignAnalyticsApi->get_campaign_delivery_confidence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignAnalyticsApi->get_campaign_delivery_confidence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign UUID | 

### Return type

[**GetCampaignDeliveryConfidence200Response**](GetCampaignDeliveryConfidence200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delivery confidence score |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_funnel**
> GetCampaignFunnel200Response get_campaign_funnel(campaign_id)

Get campaign funnel

Get the full delivery and engagement funnel for a campaign showing progression from sent through delivered, opened, and clicked.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_campaign_funnel200_response import GetCampaignFunnel200Response
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
    api_instance = mailodds.CampaignAnalyticsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Campaign UUID

    try:
        # Get campaign funnel
        api_response = api_instance.get_campaign_funnel(campaign_id)
        print("The response of CampaignAnalyticsApi->get_campaign_funnel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignAnalyticsApi->get_campaign_funnel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign UUID | 

### Return type

[**GetCampaignFunnel200Response**](GetCampaignFunnel200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign funnel analytics |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_provider_intelligence**
> GetCampaignProviderIntelligence200Response get_campaign_provider_intelligence(campaign_id)

Get provider intelligence

Get per-provider delivery and engagement breakdown for a campaign (e.g. Gmail, Outlook, Yahoo).

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_campaign_provider_intelligence200_response import GetCampaignProviderIntelligence200Response
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
    api_instance = mailodds.CampaignAnalyticsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Campaign UUID

    try:
        # Get provider intelligence
        api_response = api_instance.get_campaign_provider_intelligence(campaign_id)
        print("The response of CampaignAnalyticsApi->get_campaign_provider_intelligence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignAnalyticsApi->get_campaign_provider_intelligence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign UUID | 

### Return type

[**GetCampaignProviderIntelligence200Response**](GetCampaignProviderIntelligence200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provider intelligence data |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

