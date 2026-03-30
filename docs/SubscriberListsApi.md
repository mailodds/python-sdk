# mailodds.SubscriberListsApi

All URIs are relative to *https://api.mailodds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_subscription**](SubscriberListsApi.md#confirm_subscription) | **GET** /v1/confirm/{token} | Confirm subscription
[**create_list**](SubscriberListsApi.md#create_list) | **POST** /v1/lists | Create a subscriber list
[**delete_list**](SubscriberListsApi.md#delete_list) | **DELETE** /v1/lists/{list_id} | Delete a subscriber list
[**get_list**](SubscriberListsApi.md#get_list) | **GET** /v1/lists/{list_id} | Get a subscriber list
[**get_lists**](SubscriberListsApi.md#get_lists) | **GET** /v1/lists | List subscriber lists
[**get_subscribers**](SubscriberListsApi.md#get_subscribers) | **GET** /v1/lists/{list_id}/subscribers | List subscribers
[**subscribe**](SubscriberListsApi.md#subscribe) | **POST** /v1/subscribe/{list_id} | Subscribe to a list
[**unsubscribe_subscriber**](SubscriberListsApi.md#unsubscribe_subscriber) | **DELETE** /v1/lists/{list_id}/subscribers/{subscriber_id} | Unsubscribe a subscriber


# **confirm_subscription**
> ConfirmSubscription200Response confirm_subscription(token)

Confirm subscription

Confirm a pending subscription via the token sent in the confirmation email. No authentication required. Redirects to the list's configured redirect URL if set, otherwise returns JSON. Tokens expire after 72 hours.

### Example


```python
import mailodds
from mailodds.models.confirm_subscription200_response import ConfirmSubscription200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
)


# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.SubscriberListsApi(api_client)
    token = 'token_example' # str | Confirmation token from email

    try:
        # Confirm subscription
        api_response = api_instance.confirm_subscription(token)
        print("The response of SubscriberListsApi->confirm_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriberListsApi->confirm_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Confirmation token from email | 

### Return type

[**ConfirmSubscription200Response**](ConfirmSubscription200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription confirmed |  -  |
**302** | Redirect to configured confirmation URL |  -  |
**400** | Bad request |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_list**
> CreateList201Response create_list(create_list_request)

Create a subscriber list

Create a new subscriber list. Use lists to organize subscribers and manage double opt-in confirmation flows.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_list201_response import CreateList201Response
from mailodds.models.create_list_request import CreateListRequest
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
    api_instance = mailodds.SubscriberListsApi(api_client)
    create_list_request = mailodds.CreateListRequest() # CreateListRequest | 

    try:
        # Create a subscriber list
        api_response = api_instance.create_list(create_list_request)
        print("The response of SubscriberListsApi->create_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriberListsApi->create_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_list_request** | [**CreateListRequest**](CreateListRequest.md)|  | 

### Return type

[**CreateList201Response**](CreateList201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | List created |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list**
> DeletePolicyRule200Response delete_list(list_id)

Delete a subscriber list

Soft-delete a subscriber list. Existing subscribers are retained but the list is no longer usable.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.delete_policy_rule200_response import DeletePolicyRule200Response
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
    api_instance = mailodds.SubscriberListsApi(api_client)
    list_id = 'list_id_example' # str | List UUID

    try:
        # Delete a subscriber list
        api_response = api_instance.delete_list(list_id)
        print("The response of SubscriberListsApi->delete_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriberListsApi->delete_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| List UUID | 

### Return type

[**DeletePolicyRule200Response**](DeletePolicyRule200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List deleted |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list**
> CreateList201Response get_list(list_id)

Get a subscriber list

Get details of a specific subscriber list including subscriber and confirmed counts.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_list201_response import CreateList201Response
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
    api_instance = mailodds.SubscriberListsApi(api_client)
    list_id = 'list_id_example' # str | List UUID

    try:
        # Get a subscriber list
        api_response = api_instance.get_list(list_id)
        print("The response of SubscriberListsApi->get_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriberListsApi->get_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| List UUID | 

### Return type

[**CreateList201Response**](CreateList201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscriber list details |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lists**
> GetLists200Response get_lists(page=page, per_page=per_page)

List subscriber lists

List all subscriber lists for the authenticated account with pagination.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_lists200_response import GetLists200Response
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
    api_instance = mailodds.SubscriberListsApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    per_page = 25 # int | Items per page (optional) (default to 25)

    try:
        # List subscriber lists
        api_response = api_instance.get_lists(page=page, per_page=per_page)
        print("The response of SubscriberListsApi->get_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriberListsApi->get_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 25]

### Return type

[**GetLists200Response**](GetLists200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of subscriber lists |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscribers**
> GetSubscribers200Response get_subscribers(list_id, page=page, per_page=per_page, status=status)

List subscribers

List paginated subscribers for a specific list. Optionally filter by status.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_subscribers200_response import GetSubscribers200Response
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
    api_instance = mailodds.SubscriberListsApi(api_client)
    list_id = 'list_id_example' # str | List UUID
    page = 1 # int | Page number (optional) (default to 1)
    per_page = 50 # int | Items per page (optional) (default to 50)
    status = 'status_example' # str | Filter by subscriber status (optional)

    try:
        # List subscribers
        api_response = api_instance.get_subscribers(list_id, page=page, per_page=per_page, status=status)
        print("The response of SubscriberListsApi->get_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriberListsApi->get_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| List UUID | 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 50]
 **status** | **str**| Filter by subscriber status | [optional] 

### Return type

[**GetSubscribers200Response**](GetSubscribers200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of subscribers |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe**
> UnsubscribeSubscriber200Response subscribe(list_id, subscribe_request)

Subscribe to a list

Add a subscriber to a list and initiate the double opt-in confirmation flow. The subscriber receives a confirmation email and must click the link to confirm. Rate limited to 10 requests/min per IP and 1000/hour per account.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.subscribe_request import SubscribeRequest
from mailodds.models.unsubscribe_subscriber200_response import UnsubscribeSubscriber200Response
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
    api_instance = mailodds.SubscriberListsApi(api_client)
    list_id = 'list_id_example' # str | List UUID
    subscribe_request = mailodds.SubscribeRequest() # SubscribeRequest | 

    try:
        # Subscribe to a list
        api_response = api_instance.subscribe(list_id, subscribe_request)
        print("The response of SubscriberListsApi->subscribe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriberListsApi->subscribe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| List UUID | 
 **subscribe_request** | [**SubscribeRequest**](SubscribeRequest.md)|  | 

### Return type

[**UnsubscribeSubscriber200Response**](UnsubscribeSubscriber200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Subscriber created (pending confirmation) |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**422** | Invalid email address |  -  |
**429** | Rate limit exceeded |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_subscriber**
> UnsubscribeSubscriber200Response unsubscribe_subscriber(list_id, subscriber_id)

Unsubscribe a subscriber

Set a subscriber's status to unsubscribed. The consent record is retained for compliance.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.unsubscribe_subscriber200_response import UnsubscribeSubscriber200Response
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
    api_instance = mailodds.SubscriberListsApi(api_client)
    list_id = 'list_id_example' # str | List UUID
    subscriber_id = 'subscriber_id_example' # str | Subscriber UUID

    try:
        # Unsubscribe a subscriber
        api_response = api_instance.unsubscribe_subscriber(list_id, subscriber_id)
        print("The response of SubscriberListsApi->unsubscribe_subscriber:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriberListsApi->unsubscribe_subscriber: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| List UUID | 
 **subscriber_id** | **str**| Subscriber UUID | 

### Return type

[**UnsubscribeSubscriber200Response**](UnsubscribeSubscriber200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscriber unsubscribed |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

