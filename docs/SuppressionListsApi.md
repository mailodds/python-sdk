# mailodds.SuppressionListsApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_suppression**](SuppressionListsApi.md#add_suppression) | **POST** /v1/suppression | Add suppression entries
[**check_suppression**](SuppressionListsApi.md#check_suppression) | **POST** /v1/suppression/check | Check suppression status
[**get_suppression_stats**](SuppressionListsApi.md#get_suppression_stats) | **GET** /v1/suppression/stats | Get suppression statistics
[**list_suppression**](SuppressionListsApi.md#list_suppression) | **GET** /v1/suppression | List suppression entries
[**remove_suppression**](SuppressionListsApi.md#remove_suppression) | **DELETE** /v1/suppression | Remove suppression entries


# **add_suppression**
> AddSuppressionResponse add_suppression(add_suppression_request)

Add suppression entries

Add emails or domains to the suppression list.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.add_suppression_request import AddSuppressionRequest
from mailodds.models.add_suppression_response import AddSuppressionResponse
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
    api_instance = mailodds.SuppressionListsApi(api_client)
    add_suppression_request = mailodds.AddSuppressionRequest() # AddSuppressionRequest | 

    try:
        # Add suppression entries
        api_response = api_instance.add_suppression(add_suppression_request)
        print("The response of SuppressionListsApi->add_suppression:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionListsApi->add_suppression: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_suppression_request** | [**AddSuppressionRequest**](AddSuppressionRequest.md)|  | 

### Return type

[**AddSuppressionResponse**](AddSuppressionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entries added |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_suppression**
> SuppressionCheckResponse check_suppression(check_suppression_request)

Check suppression status

Check if an email is suppressed.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.check_suppression_request import CheckSuppressionRequest
from mailodds.models.suppression_check_response import SuppressionCheckResponse
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
    api_instance = mailodds.SuppressionListsApi(api_client)
    check_suppression_request = mailodds.CheckSuppressionRequest() # CheckSuppressionRequest | 

    try:
        # Check suppression status
        api_response = api_instance.check_suppression(check_suppression_request)
        print("The response of SuppressionListsApi->check_suppression:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionListsApi->check_suppression: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_suppression_request** | [**CheckSuppressionRequest**](CheckSuppressionRequest.md)|  | 

### Return type

[**SuppressionCheckResponse**](SuppressionCheckResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suppression check result |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_suppression_stats**
> SuppressionStatsResponse get_suppression_stats()

Get suppression statistics

Get statistics about the suppression list.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.suppression_stats_response import SuppressionStatsResponse
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
    api_instance = mailodds.SuppressionListsApi(api_client)

    try:
        # Get suppression statistics
        api_response = api_instance.get_suppression_stats()
        print("The response of SuppressionListsApi->get_suppression_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionListsApi->get_suppression_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SuppressionStatsResponse**](SuppressionStatsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suppression statistics |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_suppression**
> SuppressionListResponse list_suppression(page=page, per_page=per_page, type=type, search=search)

List suppression entries

List all suppression entries for the account.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.suppression_list_response import SuppressionListResponse
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
    api_instance = mailodds.SuppressionListsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    per_page = 50 # int |  (optional) (default to 50)
    type = 'type_example' # str |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # List suppression entries
        api_response = api_instance.list_suppression(page=page, per_page=per_page, type=type, search=search)
        print("The response of SuppressionListsApi->list_suppression:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionListsApi->list_suppression: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 50]
 **type** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**SuppressionListResponse**](SuppressionListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suppression list |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_suppression**
> RemoveSuppression200Response remove_suppression(remove_suppression_request)

Remove suppression entries

Remove emails or domains from the suppression list.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.remove_suppression200_response import RemoveSuppression200Response
from mailodds.models.remove_suppression_request import RemoveSuppressionRequest
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
    api_instance = mailodds.SuppressionListsApi(api_client)
    remove_suppression_request = mailodds.RemoveSuppressionRequest() # RemoveSuppressionRequest | 

    try:
        # Remove suppression entries
        api_response = api_instance.remove_suppression(remove_suppression_request)
        print("The response of SuppressionListsApi->remove_suppression:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionListsApi->remove_suppression: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_suppression_request** | [**RemoveSuppressionRequest**](RemoveSuppressionRequest.md)|  | 

### Return type

[**RemoveSuppression200Response**](RemoveSuppression200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entries removed |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

