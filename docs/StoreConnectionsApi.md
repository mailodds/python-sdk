# mailodds.StoreConnectionsApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_store**](StoreConnectionsApi.md#create_store) | **POST** /v1/stores | Create a store connection
[**disconnect_store**](StoreConnectionsApi.md#disconnect_store) | **DELETE** /v1/stores/{store_id} | Disconnect a store
[**get_store**](StoreConnectionsApi.md#get_store) | **GET** /v1/stores/{store_id} | Get a store connection
[**get_sync_job_errors**](StoreConnectionsApi.md#get_sync_job_errors) | **GET** /v1/stores/{store_id}/sync-jobs/{job_id}/errors | Get sync job errors
[**list_stores**](StoreConnectionsApi.md#list_stores) | **GET** /v1/stores | List store connections
[**list_sync_jobs**](StoreConnectionsApi.md#list_sync_jobs) | **GET** /v1/stores/{store_id}/sync-jobs | List sync jobs
[**trigger_sync**](StoreConnectionsApi.md#trigger_sync) | **POST** /v1/stores/{store_id}/sync | Trigger product sync
[**update_store**](StoreConnectionsApi.md#update_store) | **PUT** /v1/stores/{store_id} | Update a store connection


# **create_store**
> CreateStore201Response create_store(create_store_request)

Create a store connection

Connect an e-commerce store (WooCommerce, PrestaShop, Shopify, or product feed). After creation, trigger a sync to import products.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_store201_response import CreateStore201Response
from mailodds.models.create_store_request import CreateStoreRequest
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
    api_instance = mailodds.StoreConnectionsApi(api_client)
    create_store_request = mailodds.CreateStoreRequest() # CreateStoreRequest | 

    try:
        # Create a store connection
        api_response = api_instance.create_store(create_store_request)
        print("The response of StoreConnectionsApi->create_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreConnectionsApi->create_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_store_request** | [**CreateStoreRequest**](CreateStoreRequest.md)|  | 

### Return type

[**CreateStore201Response**](CreateStore201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Store connection created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disconnect_store**
> DisconnectStore200Response disconnect_store(store_id)

Disconnect a store

Disconnect a store and deactivate its products. Products are retained but marked inactive.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.disconnect_store200_response import DisconnectStore200Response
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
    api_instance = mailodds.StoreConnectionsApi(api_client)
    store_id = 'store_id_example' # str | 

    try:
        # Disconnect a store
        api_response = api_instance.disconnect_store(store_id)
        print("The response of StoreConnectionsApi->disconnect_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreConnectionsApi->disconnect_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  | 

### Return type

[**DisconnectStore200Response**](DisconnectStore200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Store disconnected |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_store**
> CreateStore201Response get_store(store_id)

Get a store connection

Get details of a specific store connection including sync status and product count.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_store201_response import CreateStore201Response
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
    api_instance = mailodds.StoreConnectionsApi(api_client)
    store_id = 'store_id_example' # str | 

    try:
        # Get a store connection
        api_response = api_instance.get_store(store_id)
        print("The response of StoreConnectionsApi->get_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreConnectionsApi->get_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  | 

### Return type

[**CreateStore201Response**](CreateStore201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Store connection details |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_job_errors**
> GetSyncJobErrors200Response get_sync_job_errors(store_id, job_id, page=page, per_page=per_page)

Get sync job errors

Get error details for a sync job.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_sync_job_errors200_response import GetSyncJobErrors200Response
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
    api_instance = mailodds.StoreConnectionsApi(api_client)
    store_id = 'store_id_example' # str | 
    job_id = 'job_id_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    per_page = 50 # int |  (optional) (default to 50)

    try:
        # Get sync job errors
        api_response = api_instance.get_sync_job_errors(store_id, job_id, page=page, per_page=per_page)
        print("The response of StoreConnectionsApi->get_sync_job_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreConnectionsApi->get_sync_job_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  | 
 **job_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 50]

### Return type

[**GetSyncJobErrors200Response**](GetSyncJobErrors200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sync job errors |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stores**
> ListStores200Response list_stores(status=status)

List store connections

List all store connections for the authenticated account. Optionally filter by status.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.list_stores200_response import ListStores200Response
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
    api_instance = mailodds.StoreConnectionsApi(api_client)
    status = 'status_example' # str | Filter by connection status (optional)

    try:
        # List store connections
        api_response = api_instance.list_stores(status=status)
        print("The response of StoreConnectionsApi->list_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreConnectionsApi->list_stores: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by connection status | [optional] 

### Return type

[**ListStores200Response**](ListStores200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of store connections |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sync_jobs**
> ListSyncJobs200Response list_sync_jobs(store_id, page=page, per_page=per_page)

List sync jobs

List sync job history for a store.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.list_sync_jobs200_response import ListSyncJobs200Response
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
    api_instance = mailodds.StoreConnectionsApi(api_client)
    store_id = 'store_id_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)

    try:
        # List sync jobs
        api_response = api_instance.list_sync_jobs(store_id, page=page, per_page=per_page)
        print("The response of StoreConnectionsApi->list_sync_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreConnectionsApi->list_sync_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]

### Return type

[**ListSyncJobs200Response**](ListSyncJobs200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of sync jobs |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_sync**
> SyncResponse trigger_sync(store_id, idempotency_key=idempotency_key)

Trigger product sync

Trigger a manual product sync for a store. Supports idempotency via the Idempotency-Key header (5 minute TTL).

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.sync_response import SyncResponse
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
    api_instance = mailodds.StoreConnectionsApi(api_client)
    store_id = 'store_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | Idempotency key to prevent duplicate syncs (5 min TTL) (optional)

    try:
        # Trigger product sync
        api_response = api_instance.trigger_sync(store_id, idempotency_key=idempotency_key)
        print("The response of StoreConnectionsApi->trigger_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreConnectionsApi->trigger_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  | 
 **idempotency_key** | **str**| Idempotency key to prevent duplicate syncs (5 min TTL) | [optional] 

### Return type

[**SyncResponse**](SyncResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sync scheduled |  -  |
**400** | Bad request |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_store**
> CreateStore201Response update_store(store_id, update_store_request)

Update a store connection

Update store settings such as name, sync interval, or credentials.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_store201_response import CreateStore201Response
from mailodds.models.update_store_request import UpdateStoreRequest
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
    api_instance = mailodds.StoreConnectionsApi(api_client)
    store_id = 'store_id_example' # str | 
    update_store_request = mailodds.UpdateStoreRequest() # UpdateStoreRequest | 

    try:
        # Update a store connection
        api_response = api_instance.update_store(store_id, update_store_request)
        print("The response of StoreConnectionsApi->update_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreConnectionsApi->update_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  | 
 **update_store_request** | [**UpdateStoreRequest**](UpdateStoreRequest.md)|  | 

### Return type

[**CreateStore201Response**](CreateStore201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Store connection updated |  -  |
**404** | Resource not found |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

