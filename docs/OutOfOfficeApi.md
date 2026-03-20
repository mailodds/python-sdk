# mailodds.OutOfOfficeApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_check_ooo**](OutOfOfficeApi.md#batch_check_ooo) | **POST** /v1/out-of-office/batch-check | Batch check OOO status
[**delete_ooo_contact**](OutOfOfficeApi.md#delete_ooo_contact) | **DELETE** /v1/out-of-office/{email} | Delete OOO contact
[**get_ooo_status**](OutOfOfficeApi.md#get_ooo_status) | **GET** /v1/out-of-office/{email}/status | Get OOO status for email
[**list_ooo_contacts**](OutOfOfficeApi.md#list_ooo_contacts) | **GET** /v1/out-of-office | List out-of-office contacts
[**update_ooo_contact**](OutOfOfficeApi.md#update_ooo_contact) | **PATCH** /v1/out-of-office/{email} | Update OOO contact


# **batch_check_ooo**
> BatchCheckOoo200Response batch_check_ooo(batch_check_ooo_request)

Batch check OOO status

Check OOO status for up to 1000 email addresses at once. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.batch_check_ooo200_response import BatchCheckOoo200Response
from mailodds.models.batch_check_ooo_request import BatchCheckOooRequest
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
    api_instance = mailodds.OutOfOfficeApi(api_client)
    batch_check_ooo_request = mailodds.BatchCheckOooRequest() # BatchCheckOooRequest | 

    try:
        # Batch check OOO status
        api_response = api_instance.batch_check_ooo(batch_check_ooo_request)
        print("The response of OutOfOfficeApi->batch_check_ooo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutOfOfficeApi->batch_check_ooo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_check_ooo_request** | [**BatchCheckOooRequest**](BatchCheckOooRequest.md)|  | 

### Return type

[**BatchCheckOoo200Response**](BatchCheckOoo200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch OOO check results |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ooo_contact**
> DeleteOooContact200Response delete_ooo_contact(email)

Delete OOO contact

Clear out-of-office status for an email address. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.delete_ooo_contact200_response import DeleteOooContact200Response
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
    api_instance = mailodds.OutOfOfficeApi(api_client)
    email = 'email_example' # str | 

    try:
        # Delete OOO contact
        api_response = api_instance.delete_ooo_contact(email)
        print("The response of OutOfOfficeApi->delete_ooo_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutOfOfficeApi->delete_ooo_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**DeleteOooContact200Response**](DeleteOooContact200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OOO status cleared |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ooo_status**
> GetOooStatus200Response get_ooo_status(email)

Get OOO status for email

Check if a specific email address is currently out-of-office. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_ooo_status200_response import GetOooStatus200Response
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
    api_instance = mailodds.OutOfOfficeApi(api_client)
    email = 'email_example' # str | 

    try:
        # Get OOO status for email
        api_response = api_instance.get_ooo_status(email)
        print("The response of OutOfOfficeApi->get_ooo_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutOfOfficeApi->get_ooo_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**GetOooStatus200Response**](GetOooStatus200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OOO status |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ooo_contacts**
> ListOooContacts200Response list_ooo_contacts(active_only=active_only, page=page, per_page=per_page)

List out-of-office contacts

List contacts detected as out-of-office. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.list_ooo_contacts200_response import ListOooContacts200Response
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
    api_instance = mailodds.OutOfOfficeApi(api_client)
    active_only = True # bool | Only return currently active OOO contacts (optional) (default to True)
    page = 1 # int |  (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)

    try:
        # List out-of-office contacts
        api_response = api_instance.list_ooo_contacts(active_only=active_only, page=page, per_page=per_page)
        print("The response of OutOfOfficeApi->list_ooo_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutOfOfficeApi->list_ooo_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active_only** | **bool**| Only return currently active OOO contacts | [optional] [default to True]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 100]

### Return type

[**ListOooContacts200Response**](ListOooContacts200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of OOO contacts |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ooo_contact**
> object update_ooo_contact(email, update_ooo_contact_request)

Update OOO contact

Manually set or clear out-of-office status for an email. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.update_ooo_contact_request import UpdateOooContactRequest
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
    api_instance = mailodds.OutOfOfficeApi(api_client)
    email = 'email_example' # str | 
    update_ooo_contact_request = mailodds.UpdateOooContactRequest() # UpdateOooContactRequest | 

    try:
        # Update OOO contact
        api_response = api_instance.update_ooo_contact(email, update_ooo_contact_request)
        print("The response of OutOfOfficeApi->update_ooo_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutOfOfficeApi->update_ooo_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **update_ooo_contact_request** | [**UpdateOooContactRequest**](UpdateOooContactRequest.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OOO contact updated |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

