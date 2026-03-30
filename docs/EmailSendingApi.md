# mailodds.EmailSendingApi

All URIs are relative to *https://api.mailodds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deliver_batch**](EmailSendingApi.md#deliver_batch) | **POST** /v1/deliver/batch | Send to multiple recipients (max 100)
[**deliver_email**](EmailSendingApi.md#deliver_email) | **POST** /v1/deliver | Send a single email


# **deliver_batch**
> BatchDeliverResponse deliver_batch(batch_deliver_request)

Send to multiple recipients (max 100)

Send a single message to up to 100 recipients. Shares the same message body across all recipients. Each recipient is processed independently.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.batch_deliver_request import BatchDeliverRequest
from mailodds.models.batch_deliver_response import BatchDeliverResponse
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
    api_instance = mailodds.EmailSendingApi(api_client)
    batch_deliver_request = mailodds.BatchDeliverRequest() # BatchDeliverRequest | 

    try:
        # Send to multiple recipients (max 100)
        api_response = api_instance.deliver_batch(batch_deliver_request)
        print("The response of EmailSendingApi->deliver_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSendingApi->deliver_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_deliver_request** | [**BatchDeliverRequest**](BatchDeliverRequest.md)|  | 

### Return type

[**BatchDeliverResponse**](BatchDeliverResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Batch accepted for delivery |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deliver_email**
> DeliverResponse deliver_email(deliver_request)

Send a single email

Send a transactional email through the safety pipeline. Validates recipients, checks domain ownership, and queues for delivery. Requires a verified sending domain.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.deliver_request import DeliverRequest
from mailodds.models.deliver_response import DeliverResponse
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
    api_instance = mailodds.EmailSendingApi(api_client)
    deliver_request = mailodds.DeliverRequest() # DeliverRequest | 

    try:
        # Send a single email
        api_response = api_instance.deliver_email(deliver_request)
        print("The response of EmailSendingApi->deliver_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSendingApi->deliver_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deliver_request** | [**DeliverRequest**](DeliverRequest.md)|  | 

### Return type

[**DeliverResponse**](DeliverResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Email accepted for delivery |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

