# mailodds.SpamChecksApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_spam_check**](SpamChecksApi.md#get_spam_check) | **GET** /v1/spam-checks/{check_id} | Get spam check
[**list_spam_checks**](SpamChecksApi.md#list_spam_checks) | **GET** /v1/spam-checks | List spam checks
[**run_spam_check**](SpamChecksApi.md#run_spam_check) | **POST** /v1/spam-checks | Run spam check


# **get_spam_check**
> RunSpamCheck201Response get_spam_check(check_id)

Get spam check

Get the detailed result of a specific spam check.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.run_spam_check201_response import RunSpamCheck201Response
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
    api_instance = mailodds.SpamChecksApi(api_client)
    check_id = 'check_id_example' # str | Spam check UUID

    try:
        # Get spam check
        api_response = api_instance.get_spam_check(check_id)
        print("The response of SpamChecksApi->get_spam_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamChecksApi->get_spam_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**| Spam check UUID | 

### Return type

[**RunSpamCheck201Response**](RunSpamCheck201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Spam check details |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_spam_checks**
> ListSpamChecks200Response list_spam_checks(page=page, per_page=per_page)

List spam checks

List past spam check results with pagination.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.list_spam_checks200_response import ListSpamChecks200Response
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
    api_instance = mailodds.SpamChecksApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)

    try:
        # List spam checks
        api_response = api_instance.list_spam_checks(page=page, per_page=per_page)
        print("The response of SpamChecksApi->list_spam_checks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamChecksApi->list_spam_checks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]

### Return type

[**ListSpamChecks200Response**](ListSpamChecks200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of spam checks |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_spam_check**
> RunSpamCheck201Response run_spam_check(run_spam_check_request)

Run spam check

Run backend spam checks on email sending parameters. Checks domain reputation, link safety, and subject line quality.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.run_spam_check201_response import RunSpamCheck201Response
from mailodds.models.run_spam_check_request import RunSpamCheckRequest
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
    api_instance = mailodds.SpamChecksApi(api_client)
    run_spam_check_request = mailodds.RunSpamCheckRequest() # RunSpamCheckRequest | 

    try:
        # Run spam check
        api_response = api_instance.run_spam_check(run_spam_check_request)
        print("The response of SpamChecksApi->run_spam_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamChecksApi->run_spam_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_spam_check_request** | [**RunSpamCheckRequest**](RunSpamCheckRequest.md)|  | 

### Return type

[**RunSpamCheck201Response**](RunSpamCheck201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Spam check result |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

