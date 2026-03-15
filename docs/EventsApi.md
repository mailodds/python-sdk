# mailodds.EventsApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**track_event**](EventsApi.md#track_event) | **POST** /v1/events/track | Track a commerce event


# **track_event**
> TrackEventResponse track_event(track_event_request)

Track a commerce event

Ingest a commerce event (purchase, cart abandonment, browse, wishlist, review, etc.). Supports idempotency via the idempotency_key field (5 minute Redis TTL + DB unique constraint).

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.track_event_request import TrackEventRequest
from mailodds.models.track_event_response import TrackEventResponse
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
    api_instance = mailodds.EventsApi(api_client)
    track_event_request = mailodds.TrackEventRequest() # TrackEventRequest | 

    try:
        # Track a commerce event
        api_response = api_instance.track_event(track_event_request)
        print("The response of EventsApi->track_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->track_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **track_event_request** | [**TrackEventRequest**](TrackEventRequest.md)|  | 

### Return type

[**TrackEventResponse**](TrackEventResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Event created |  -  |
**200** | Idempotent duplicate (event already exists) |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

