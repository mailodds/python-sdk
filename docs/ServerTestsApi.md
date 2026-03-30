# mailodds.ServerTestsApi

All URIs are relative to *https://api.mailodds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_server_test**](ServerTestsApi.md#get_server_test) | **GET** /v1/server-tests/{test_id} | Get server test
[**list_server_tests**](ServerTestsApi.md#list_server_tests) | **GET** /v1/server-tests | List server tests
[**run_server_test**](ServerTestsApi.md#run_server_test) | **POST** /v1/server-tests | Run server test


# **get_server_test**
> RunServerTest201Response get_server_test(test_id)

Get server test

Get the detailed results of a specific server test.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.run_server_test201_response import RunServerTest201Response
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
    api_instance = mailodds.ServerTestsApi(api_client)
    test_id = 'test_id_example' # str | 

    try:
        # Get server test
        api_response = api_instance.get_server_test(test_id)
        print("The response of ServerTestsApi->get_server_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerTestsApi->get_server_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**|  | 

### Return type

[**RunServerTest201Response**](RunServerTest201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server test details |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_server_tests**
> ListServerTests200Response list_server_tests(page=page, per_page=per_page)

List server tests

List past server test results with pagination.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.list_server_tests200_response import ListServerTests200Response
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
    api_instance = mailodds.ServerTestsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)

    try:
        # List server tests
        api_response = api_instance.list_server_tests(page=page, per_page=per_page)
        print("The response of ServerTestsApi->list_server_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerTestsApi->list_server_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]

### Return type

[**ListServerTests200Response**](ListServerTests200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of server tests |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_server_test**
> RunServerTest201Response run_server_test(run_server_test_request)

Run server test

Run an SMTP handshake test and MX configuration audit for a domain.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.run_server_test201_response import RunServerTest201Response
from mailodds.models.run_server_test_request import RunServerTestRequest
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
    api_instance = mailodds.ServerTestsApi(api_client)
    run_server_test_request = mailodds.RunServerTestRequest() # RunServerTestRequest | 

    try:
        # Run server test
        api_response = api_instance.run_server_test(run_server_test_request)
        print("The response of ServerTestsApi->run_server_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerTestsApi->run_server_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_server_test_request** | [**RunServerTestRequest**](RunServerTestRequest.md)|  | 

### Return type

[**RunServerTest201Response**](RunServerTest201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Test result |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

