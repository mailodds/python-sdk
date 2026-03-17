# mailodds.ReputationApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reputation**](ReputationApi.md#get_reputation) | **GET** /v1/reputation | Get account reputation
[**get_reputation_timeline**](ReputationApi.md#get_reputation_timeline) | **GET** /v1/reputation/timeline | Get reputation timeline


# **get_reputation**
> GetReputation200Response get_reputation(period=period)

Get account reputation

Get the aggregate reputation score and breakdown for the account.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_reputation200_response import GetReputation200Response
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
    api_instance = mailodds.ReputationApi(api_client)
    period = 7d # str | Evaluation period (optional) (default to 7d)

    try:
        # Get account reputation
        api_response = api_instance.get_reputation(period=period)
        print("The response of ReputationApi->get_reputation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReputationApi->get_reputation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| Evaluation period | [optional] [default to 7d]

### Return type

[**GetReputation200Response**](GetReputation200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account reputation |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reputation_timeline**
> GetReputationTimeline200Response get_reputation_timeline(period=period)

Get reputation timeline

Get reputation metrics over time.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_reputation_timeline200_response import GetReputationTimeline200Response
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
    api_instance = mailodds.ReputationApi(api_client)
    period = 30d # str | Timeline period (optional) (default to 30d)

    try:
        # Get reputation timeline
        api_response = api_instance.get_reputation_timeline(period=period)
        print("The response of ReputationApi->get_reputation_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReputationApi->get_reputation_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| Timeline period | [optional] [default to 30d]

### Return type

[**GetReputationTimeline200Response**](GetReputationTimeline200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reputation timeline |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

