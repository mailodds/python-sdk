# mailodds.BlacklistMonitoringApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_blacklist_monitor**](BlacklistMonitoringApi.md#add_blacklist_monitor) | **POST** /v1/blacklist-monitors | Add blacklist monitor
[**get_blacklist_history**](BlacklistMonitoringApi.md#get_blacklist_history) | **GET** /v1/blacklist-monitors/{monitor_id}/history | Get blacklist check history
[**list_blacklist_monitors**](BlacklistMonitoringApi.md#list_blacklist_monitors) | **GET** /v1/blacklist-monitors | List blacklist monitors
[**run_blacklist_check**](BlacklistMonitoringApi.md#run_blacklist_check) | **POST** /v1/blacklist-monitors/{monitor_id}/check | Run blacklist check


# **add_blacklist_monitor**
> AddBlacklistMonitor201Response add_blacklist_monitor(add_blacklist_monitor_request)

Add blacklist monitor

Add an IP address or domain to monitor against DNS blacklists. An initial check is run immediately.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.add_blacklist_monitor201_response import AddBlacklistMonitor201Response
from mailodds.models.add_blacklist_monitor_request import AddBlacklistMonitorRequest
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
    api_instance = mailodds.BlacklistMonitoringApi(api_client)
    add_blacklist_monitor_request = mailodds.AddBlacklistMonitorRequest() # AddBlacklistMonitorRequest | 

    try:
        # Add blacklist monitor
        api_response = api_instance.add_blacklist_monitor(add_blacklist_monitor_request)
        print("The response of BlacklistMonitoringApi->add_blacklist_monitor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlacklistMonitoringApi->add_blacklist_monitor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_blacklist_monitor_request** | [**AddBlacklistMonitorRequest**](AddBlacklistMonitorRequest.md)|  | 

### Return type

[**AddBlacklistMonitor201Response**](AddBlacklistMonitor201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Monitor created with initial check result |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blacklist_history**
> GetBlacklistHistory200Response get_blacklist_history(monitor_id, page=page, per_page=per_page)

Get blacklist check history

Get the listing and delisting timeline for a monitored IP or domain.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_blacklist_history200_response import GetBlacklistHistory200Response
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
    api_instance = mailodds.BlacklistMonitoringApi(api_client)
    monitor_id = 'monitor_id_example' # str | Monitor UUID
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)

    try:
        # Get blacklist check history
        api_response = api_instance.get_blacklist_history(monitor_id, page=page, per_page=per_page)
        print("The response of BlacklistMonitoringApi->get_blacklist_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlacklistMonitoringApi->get_blacklist_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_id** | **str**| Monitor UUID | 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]

### Return type

[**GetBlacklistHistory200Response**](GetBlacklistHistory200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Check history |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_blacklist_monitors**
> ListBlacklistMonitors200Response list_blacklist_monitors()

List blacklist monitors

List all blacklist monitors for the authenticated account.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.list_blacklist_monitors200_response import ListBlacklistMonitors200Response
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
    api_instance = mailodds.BlacklistMonitoringApi(api_client)

    try:
        # List blacklist monitors
        api_response = api_instance.list_blacklist_monitors()
        print("The response of BlacklistMonitoringApi->list_blacklist_monitors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlacklistMonitoringApi->list_blacklist_monitors: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListBlacklistMonitors200Response**](ListBlacklistMonitors200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of monitors |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_blacklist_check**
> RunBlacklistCheck200Response run_blacklist_check(monitor_id)

Run blacklist check

Run an on-demand DNSBL check for a monitored IP or domain.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.run_blacklist_check200_response import RunBlacklistCheck200Response
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
    api_instance = mailodds.BlacklistMonitoringApi(api_client)
    monitor_id = 'monitor_id_example' # str | Monitor UUID

    try:
        # Run blacklist check
        api_response = api_instance.run_blacklist_check(monitor_id)
        print("The response of BlacklistMonitoringApi->run_blacklist_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlacklistMonitoringApi->run_blacklist_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_id** | **str**| Monitor UUID | 

### Return type

[**RunBlacklistCheck200Response**](RunBlacklistCheck200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Check result |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

