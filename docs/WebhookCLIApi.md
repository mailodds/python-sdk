# mailodds.WebhookCLIApi

All URIs are relative to *https://api.mailodds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_cli_session**](WebhookCLIApi.md#create_webhook_cli_session) | **POST** /v1/webhook-cli/sessions | Create CLI forwarding session
[**delete_webhook_cli_session**](WebhookCLIApi.md#delete_webhook_cli_session) | **DELETE** /v1/webhook-cli/sessions/{session_id} | Close CLI session
[**list_webhook_deliveries**](WebhookCLIApi.md#list_webhook_deliveries) | **GET** /v1/webhook-cli/deliveries | List recent webhook deliveries
[**replay_webhook_delivery**](WebhookCLIApi.md#replay_webhook_delivery) | **POST** /v1/webhook-cli/deliveries/{delivery_id}/replay | Replay webhook delivery


# **create_webhook_cli_session**
> CreateWebhookCliSession201Response create_webhook_cli_session(create_webhook_cli_session_request=create_webhook_cli_session_request)

Create CLI forwarding session

Register a new session for receiving webhook events via SSE.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_webhook_cli_session201_response import CreateWebhookCliSession201Response
from mailodds.models.create_webhook_cli_session_request import CreateWebhookCliSessionRequest
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
    api_instance = mailodds.WebhookCLIApi(api_client)
    create_webhook_cli_session_request = mailodds.CreateWebhookCliSessionRequest() # CreateWebhookCliSessionRequest |  (optional)

    try:
        # Create CLI forwarding session
        api_response = api_instance.create_webhook_cli_session(create_webhook_cli_session_request=create_webhook_cli_session_request)
        print("The response of WebhookCLIApi->create_webhook_cli_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookCLIApi->create_webhook_cli_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_cli_session_request** | [**CreateWebhookCliSessionRequest**](CreateWebhookCliSessionRequest.md)|  | [optional] 

### Return type

[**CreateWebhookCliSession201Response**](CreateWebhookCliSession201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Session created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_cli_session**
> DeleteWebhookCliSession200Response delete_webhook_cli_session(session_id)

Close CLI session

Close a webhook CLI forwarding session.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.delete_webhook_cli_session200_response import DeleteWebhookCliSession200Response
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
    api_instance = mailodds.WebhookCLIApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Close CLI session
        api_response = api_instance.delete_webhook_cli_session(session_id)
        print("The response of WebhookCLIApi->delete_webhook_cli_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookCLIApi->delete_webhook_cli_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**DeleteWebhookCliSession200Response**](DeleteWebhookCliSession200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Session closed |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhook_deliveries**
> ListWebhookDeliveries200Response list_webhook_deliveries(limit=limit)

List recent webhook deliveries

List recent webhook deliveries for replay.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.list_webhook_deliveries200_response import ListWebhookDeliveries200Response
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
    api_instance = mailodds.WebhookCLIApi(api_client)
    limit = 50 # int | Maximum deliveries to return (optional) (default to 50)

    try:
        # List recent webhook deliveries
        api_response = api_instance.list_webhook_deliveries(limit=limit)
        print("The response of WebhookCLIApi->list_webhook_deliveries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookCLIApi->list_webhook_deliveries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum deliveries to return | [optional] [default to 50]

### Return type

[**ListWebhookDeliveries200Response**](ListWebhookDeliveries200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of recent webhook deliveries |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replay_webhook_delivery**
> ReplayWebhookDelivery200Response replay_webhook_delivery(delivery_id)

Replay webhook delivery

Replay a historical webhook delivery to active CLI sessions.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.replay_webhook_delivery200_response import ReplayWebhookDelivery200Response
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
    api_instance = mailodds.WebhookCLIApi(api_client)
    delivery_id = 56 # int | 

    try:
        # Replay webhook delivery
        api_response = api_instance.replay_webhook_delivery(delivery_id)
        print("The response of WebhookCLIApi->replay_webhook_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookCLIApi->replay_webhook_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | **int**|  | 

### Return type

[**ReplayWebhookDelivery200Response**](ReplayWebhookDelivery200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delivery replayed |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

