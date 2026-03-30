# mailodds.BounceAnalysisApi

All URIs are relative to *https://api.mailodds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bounce_analysis**](BounceAnalysisApi.md#create_bounce_analysis) | **POST** /v1/bounce-analyses | Analyze bounce logs
[**cross_reference_bounces**](BounceAnalysisApi.md#cross_reference_bounces) | **GET** /v1/bounce-analyses/{analysis_id}/cross-reference | Cross-reference bounces with validation logs
[**delete_bounce_analysis**](BounceAnalysisApi.md#delete_bounce_analysis) | **DELETE** /v1/bounce-analyses/{analysis_id} | Delete bounce analysis
[**get_bounce_analysis**](BounceAnalysisApi.md#get_bounce_analysis) | **GET** /v1/bounce-analyses/{analysis_id} | Get bounce analysis
[**get_bounce_records**](BounceAnalysisApi.md#get_bounce_records) | **GET** /v1/bounce-analyses/{analysis_id}/records | Get bounce records


# **create_bounce_analysis**
> BounceAnalysisResponse create_bounce_analysis(create_bounce_analysis_request)

Analyze bounce logs

Submit bounce log data for analysis. Identifies patterns, categorizes bounce types, and provides remediation recommendations.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.bounce_analysis_response import BounceAnalysisResponse
from mailodds.models.create_bounce_analysis_request import CreateBounceAnalysisRequest
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
    api_instance = mailodds.BounceAnalysisApi(api_client)
    create_bounce_analysis_request = mailodds.CreateBounceAnalysisRequest() # CreateBounceAnalysisRequest | 

    try:
        # Analyze bounce logs
        api_response = api_instance.create_bounce_analysis(create_bounce_analysis_request)
        print("The response of BounceAnalysisApi->create_bounce_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BounceAnalysisApi->create_bounce_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_bounce_analysis_request** | [**CreateBounceAnalysisRequest**](CreateBounceAnalysisRequest.md)|  | 

### Return type

[**BounceAnalysisResponse**](BounceAnalysisResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Bounce analysis created |  -  |
**404** | Resource not found |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cross_reference_bounces**
> CrossReferenceBounces200Response cross_reference_bounces(analysis_id)

Cross-reference bounces with validation logs

Match bounced emails against your validation history to identify emails that were validated as deliverable but later bounced.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.cross_reference_bounces200_response import CrossReferenceBounces200Response
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
    api_instance = mailodds.BounceAnalysisApi(api_client)
    analysis_id = 'analysis_id_example' # str | Bounce analysis UUID

    try:
        # Cross-reference bounces with validation logs
        api_response = api_instance.cross_reference_bounces(analysis_id)
        print("The response of BounceAnalysisApi->cross_reference_bounces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BounceAnalysisApi->cross_reference_bounces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Bounce analysis UUID | 

### Return type

[**CrossReferenceBounces200Response**](CrossReferenceBounces200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cross-reference results |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bounce_analysis**
> DeletePolicyRule200Response delete_bounce_analysis(analysis_id)

Delete bounce analysis

Delete a bounce analysis and all associated records.

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
    api_instance = mailodds.BounceAnalysisApi(api_client)
    analysis_id = 'analysis_id_example' # str | Bounce analysis ID

    try:
        # Delete bounce analysis
        api_response = api_instance.delete_bounce_analysis(analysis_id)
        print("The response of BounceAnalysisApi->delete_bounce_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BounceAnalysisApi->delete_bounce_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Bounce analysis ID | 

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
**200** | Bounce analysis deleted |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bounce_analysis**
> BounceAnalysisResponse get_bounce_analysis(analysis_id)

Get bounce analysis

Get the results of a bounce analysis including category breakdown, top offenders, and recommendations.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.bounce_analysis_response import BounceAnalysisResponse
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
    api_instance = mailodds.BounceAnalysisApi(api_client)
    analysis_id = 'analysis_id_example' # str | Bounce analysis UUID

    try:
        # Get bounce analysis
        api_response = api_instance.get_bounce_analysis(analysis_id)
        print("The response of BounceAnalysisApi->get_bounce_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BounceAnalysisApi->get_bounce_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Bounce analysis UUID | 

### Return type

[**BounceAnalysisResponse**](BounceAnalysisResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bounce analysis results |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bounce_records**
> GetBounceRecords200Response get_bounce_records(analysis_id, page=page, per_page=per_page, type=type)

Get bounce records

Get individual bounce records from an analysis with pagination.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_bounce_records200_response import GetBounceRecords200Response
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
    api_instance = mailodds.BounceAnalysisApi(api_client)
    analysis_id = 'analysis_id_example' # str | Bounce analysis UUID
    page = 1 # int | Page number (optional) (default to 1)
    per_page = 50 # int | Items per page (optional) (default to 50)
    type = 'type_example' # str | Filter by bounce type (optional)

    try:
        # Get bounce records
        api_response = api_instance.get_bounce_records(analysis_id, page=page, per_page=per_page, type=type)
        print("The response of BounceAnalysisApi->get_bounce_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BounceAnalysisApi->get_bounce_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Bounce analysis UUID | 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 50]
 **type** | **str**| Filter by bounce type | [optional] 

### Return type

[**GetBounceRecords200Response**](GetBounceRecords200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bounce records |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

