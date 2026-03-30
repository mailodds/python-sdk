# mailodds.DeliverabilityAdvisorApi

All URIs are relative to *https://api.mailodds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dismiss_deliverability_recommendation**](DeliverabilityAdvisorApi.md#dismiss_deliverability_recommendation) | **POST** /v1/deliverability/recommendations/{recommendation_id}/dismiss | Dismiss a deliverability recommendation
[**get_deliverability_recommendations**](DeliverabilityAdvisorApi.md#get_deliverability_recommendations) | **GET** /v1/deliverability/recommendations | Get deliverability recommendations


# **dismiss_deliverability_recommendation**
> dismiss_deliverability_recommendation(recommendation_id)

Dismiss a deliverability recommendation

Dismiss a deliverability recommendation so it no longer appears.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
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
    api_instance = mailodds.DeliverabilityAdvisorApi(api_client)
    recommendation_id = 'recommendation_id_example' # str | 

    try:
        # Dismiss a deliverability recommendation
        api_instance.dismiss_deliverability_recommendation(recommendation_id)
    except Exception as e:
        print("Exception when calling DeliverabilityAdvisorApi->dismiss_deliverability_recommendation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommendation_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dismiss a deliverability recommendation |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deliverability_recommendations**
> get_deliverability_recommendations()

Get deliverability recommendations

Retrieve actionable deliverability recommendations for the account.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
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
    api_instance = mailodds.DeliverabilityAdvisorApi(api_client)

    try:
        # Get deliverability recommendations
        api_instance.get_deliverability_recommendations()
    except Exception as e:
        print("Exception when calling DeliverabilityAdvisorApi->get_deliverability_recommendations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get deliverability recommendations |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

