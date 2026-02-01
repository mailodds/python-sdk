# mailodds.SystemApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_telemetry_summary**](SystemApi.md#get_telemetry_summary) | **GET** /v1/telemetry/summary | Get validation telemetry
[**health_check**](SystemApi.md#health_check) | **GET** /health | Health check


# **get_telemetry_summary**
> TelemetrySummary get_telemetry_summary(window=window)

Get validation telemetry

Get validation metrics for your account. Useful for building dashboards and monitoring. Supports ETag caching.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.telemetry_summary import TelemetrySummary
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
    api_instance = mailodds.SystemApi(api_client)
    window = 24h # str | Time window for metrics (optional) (default to 24h)

    try:
        # Get validation telemetry
        api_response = api_instance.get_telemetry_summary(window=window)
        print("The response of SystemApi->get_telemetry_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_telemetry_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **window** | **str**| Time window for metrics | [optional] [default to 24h]

### Return type

[**TelemetrySummary**](TelemetrySummary.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Telemetry summary |  * ETag - Hash of response for caching <br>  * Cache-Control - Caching directive <br>  |
**304** | Not Modified - use cached response |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_check**
> HealthCheck200Response health_check()

Health check

Check API health status. No authentication required.

### Example


```python
import mailodds
from mailodds.models.health_check200_response import HealthCheck200Response
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
    api_instance = mailodds.SystemApi(api_client)

    try:
        # Health check
        api_response = api_instance.health_check()
        print("The response of SystemApi->health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthCheck200Response**](HealthCheck200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API is healthy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

