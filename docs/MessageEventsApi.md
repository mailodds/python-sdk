# mailodds.MessageEventsApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_message_events**](MessageEventsApi.md#get_message_events) | **GET** /v1/message-events | Get message events


# **get_message_events**
> GetMessageEvents200Response get_message_events(message_id)

Get message events

Get delivery and engagement events for a specific sent message. Returns events in chronological order with bot detection.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_message_events200_response import GetMessageEvents200Response
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
    api_instance = mailodds.MessageEventsApi(api_client)
    message_id = 'message_id_example' # str | UUID of the sent message

    try:
        # Get message events
        api_response = api_instance.get_message_events(message_id)
        print("The response of MessageEventsApi->get_message_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessageEventsApi->get_message_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| UUID of the sent message | 

### Return type

[**GetMessageEvents200Response**](GetMessageEvents200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message events with summary |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

