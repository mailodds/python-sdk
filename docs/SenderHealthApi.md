# mailodds.SenderHealthApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sender_health**](SenderHealthApi.md#get_sender_health) | **GET** /v1/sender-health | Get sender health score
[**get_sender_health_trend**](SenderHealthApi.md#get_sender_health_trend) | **GET** /v1/sender-health/trend | Get sender health trend


# **get_sender_health**
> GetSenderHealth200Response get_sender_health(period=period)

Get sender health score

Get an aggregate sender health score (0-100) across all sending domains. Factors in delivery rate, bounce rate, complaint rate, and authentication status.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_sender_health200_response import GetSenderHealth200Response
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
    api_instance = mailodds.SenderHealthApi(api_client)
    period = 30d # str | Time period for health calculation (optional) (default to 30d)

    try:
        # Get sender health score
        api_response = api_instance.get_sender_health(period=period)
        print("The response of SenderHealthApi->get_sender_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenderHealthApi->get_sender_health: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| Time period for health calculation | [optional] [default to 30d]

### Return type

[**GetSenderHealth200Response**](GetSenderHealth200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sender health score |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender_health_trend**
> GetSenderHealthTrend200Response get_sender_health_trend(period=period)

Get sender health trend

Get historical sender health scores over time for trend analysis. Returns daily data points for the requested period.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_sender_health_trend200_response import GetSenderHealthTrend200Response
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
    api_instance = mailodds.SenderHealthApi(api_client)
    period = 30d # str | Time period for trend data (optional) (default to 30d)

    try:
        # Get sender health trend
        api_response = api_instance.get_sender_health_trend(period=period)
        print("The response of SenderHealthApi->get_sender_health_trend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenderHealthApi->get_sender_health_trend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| Time period for trend data | [optional] [default to 30d]

### Return type

[**GetSenderHealthTrend200Response**](GetSenderHealthTrend200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sender health trend |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

