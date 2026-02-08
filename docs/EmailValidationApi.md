# mailodds.EmailValidationApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_batch**](EmailValidationApi.md#validate_batch) | **POST** /v1/validate/batch | Validate multiple emails (sync)
[**validate_email**](EmailValidationApi.md#validate_email) | **POST** /v1/validate | Validate single email


# **validate_batch**
> ValidateBatch200Response validate_batch(validate_batch_request)

Validate multiple emails (sync)

Validate up to 100 email addresses synchronously. For larger lists, use the bulk jobs API.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.validate_batch200_response import ValidateBatch200Response
from mailodds.models.validate_batch_request import ValidateBatchRequest
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
    api_instance = mailodds.EmailValidationApi(api_client)
    validate_batch_request = mailodds.ValidateBatchRequest() # ValidateBatchRequest | 

    try:
        # Validate multiple emails (sync)
        api_response = api_instance.validate_batch(validate_batch_request)
        print("The response of EmailValidationApi->validate_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailValidationApi->validate_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_batch_request** | [**ValidateBatchRequest**](ValidateBatchRequest.md)|  | 

### Return type

[**ValidateBatch200Response**](ValidateBatch200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch validation results |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_email**
> ValidationResponse validate_email(validate_request)

Validate single email

Validate a single email address. Returns detailed validation results including status, sub-status, and recommended action.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.validate_request import ValidateRequest
from mailodds.models.validation_response import ValidationResponse
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
    api_instance = mailodds.EmailValidationApi(api_client)
    validate_request = mailodds.ValidateRequest() # ValidateRequest | 

    try:
        # Validate single email
        api_response = api_instance.validate_email(validate_request)
        print("The response of EmailValidationApi->validate_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailValidationApi->validate_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_request** | [**ValidateRequest**](ValidateRequest.md)|  | 

### Return type

[**ValidationResponse**](ValidationResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Validation result |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

