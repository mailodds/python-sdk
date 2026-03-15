# mailodds.ContactListsApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_to_contact_list**](ContactListsApi.md#append_to_contact_list) | **POST** /v1/contact-lists/{list_id}/append | Append to contact list
[**create_contact_list**](ContactListsApi.md#create_contact_list) | **POST** /v1/contact-lists | Create contact list
[**delete_contact_list**](ContactListsApi.md#delete_contact_list) | **DELETE** /v1/contact-lists/{list_id} | Delete a contact list
[**get_inactive_contacts_report**](ContactListsApi.md#get_inactive_contacts_report) | **GET** /v1/contacts/inactive-report | Get inactive contacts report
[**list_contact_lists**](ContactListsApi.md#list_contact_lists) | **GET** /v1/contact-lists | List contact lists
[**query_contact_list**](ContactListsApi.md#query_contact_list) | **POST** /v1/contact-lists/{list_id}/query | Query contact list


# **append_to_contact_list**
> AppendToContactList200Response append_to_contact_list(list_id, append_to_contact_list_request)

Append to contact list

Append validated emails from additional jobs to an existing contact list. Duplicates are automatically skipped.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.append_to_contact_list200_response import AppendToContactList200Response
from mailodds.models.append_to_contact_list_request import AppendToContactListRequest
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
    api_instance = mailodds.ContactListsApi(api_client)
    list_id = 'list_id_example' # str | Contact list UUID
    append_to_contact_list_request = mailodds.AppendToContactListRequest() # AppendToContactListRequest | 

    try:
        # Append to contact list
        api_response = api_instance.append_to_contact_list(list_id, append_to_contact_list_request)
        print("The response of ContactListsApi->append_to_contact_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactListsApi->append_to_contact_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| Contact list UUID | 
 **append_to_contact_list_request** | [**AppendToContactListRequest**](AppendToContactListRequest.md)|  | 

### Return type

[**AppendToContactList200Response**](AppendToContactList200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Append result |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact_list**
> CreateContactList201Response create_contact_list(create_contact_list_request)

Create contact list

Create a new contact list from one or more completed validation jobs. Only accepted (valid) emails are included.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_contact_list201_response import CreateContactList201Response
from mailodds.models.create_contact_list_request import CreateContactListRequest
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
    api_instance = mailodds.ContactListsApi(api_client)
    create_contact_list_request = mailodds.CreateContactListRequest() # CreateContactListRequest | 

    try:
        # Create contact list
        api_response = api_instance.create_contact_list(create_contact_list_request)
        print("The response of ContactListsApi->create_contact_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactListsApi->create_contact_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contact_list_request** | [**CreateContactListRequest**](CreateContactListRequest.md)|  | 

### Return type

[**CreateContactList201Response**](CreateContactList201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Contact list created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_list**
> DeletePolicyRule200Response delete_contact_list(list_id)

Delete a contact list

Permanently delete a contact list and all its entries.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.delete_policy_rule200_response import DeletePolicyRule200Response
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
    api_instance = mailodds.ContactListsApi(api_client)
    list_id = 'list_id_example' # str | Contact list UUID

    try:
        # Delete a contact list
        api_response = api_instance.delete_contact_list(list_id)
        print("The response of ContactListsApi->delete_contact_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactListsApi->delete_contact_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| Contact list UUID | 

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
**200** | Contact list deleted |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inactive_contacts_report**
> GetInactiveContactsReport200Response get_inactive_contacts_report(days=days)

Get inactive contacts report

Get a report of contacts across all lists with no engagement activity (opens, clicks) in the specified period.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_inactive_contacts_report200_response import GetInactiveContactsReport200Response
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
    api_instance = mailodds.ContactListsApi(api_client)
    days = 90 # int | Inactivity threshold in days (optional) (default to 90)

    try:
        # Get inactive contacts report
        api_response = api_instance.get_inactive_contacts_report(days=days)
        print("The response of ContactListsApi->get_inactive_contacts_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactListsApi->get_inactive_contacts_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Inactivity threshold in days | [optional] [default to 90]

### Return type

[**GetInactiveContactsReport200Response**](GetInactiveContactsReport200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inactive contacts report |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contact_lists**
> ListContactLists200Response list_contact_lists(page=page, per_page=per_page)

List contact lists

List contact lists for the authenticated account. Contact lists are built from validated email jobs.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.list_contact_lists200_response import ListContactLists200Response
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
    api_instance = mailodds.ContactListsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)

    try:
        # List contact lists
        api_response = api_instance.list_contact_lists(page=page, per_page=per_page)
        print("The response of ContactListsApi->list_contact_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactListsApi->list_contact_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]

### Return type

[**ListContactLists200Response**](ListContactLists200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of contact lists |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_contact_list**
> QueryContactList200Response query_contact_list(list_id, query_contact_list_request)

Query contact list

Query contact list entries with structured filters. Supports filtering by validation status, domain, and other attributes.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.query_contact_list200_response import QueryContactList200Response
from mailodds.models.query_contact_list_request import QueryContactListRequest
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
    api_instance = mailodds.ContactListsApi(api_client)
    list_id = 'list_id_example' # str | Contact list UUID
    query_contact_list_request = mailodds.QueryContactListRequest() # QueryContactListRequest | 

    try:
        # Query contact list
        api_response = api_instance.query_contact_list(list_id, query_contact_list_request)
        print("The response of ContactListsApi->query_contact_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactListsApi->query_contact_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| Contact list UUID | 
 **query_contact_list_request** | [**QueryContactListRequest**](QueryContactListRequest.md)|  | 

### Return type

[**QueryContactList200Response**](QueryContactList200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query results |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

