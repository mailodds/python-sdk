# mailodds.ContactListsApi

All URIs are relative to *https://api.mailodds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contact**](ContactListsApi.md#add_contact) | **POST** /v1/contact-lists/{list_id}/contacts | Add contact to list
[**append_to_contact_list**](ContactListsApi.md#append_to_contact_list) | **POST** /v1/contact-lists/{list_id}/append | Append to contact list
[**create_contact_list**](ContactListsApi.md#create_contact_list) | **POST** /v1/contact-lists | Create contact list
[**delete_contact**](ContactListsApi.md#delete_contact) | **DELETE** /v1/contact-lists/{list_id}/contacts/{contact_id} | Delete contact
[**delete_contact_list**](ContactListsApi.md#delete_contact_list) | **DELETE** /v1/contact-lists/{list_id} | Delete a contact list
[**export_contact_list**](ContactListsApi.md#export_contact_list) | **GET** /v1/contact-lists/{list_id}/export | Export contact list
[**get_inactive_contacts_report**](ContactListsApi.md#get_inactive_contacts_report) | **GET** /v1/contacts/inactive-report | Get inactive contacts report
[**import_contact_list**](ContactListsApi.md#import_contact_list) | **POST** /v1/contact-lists/{list_id}/import | Import contacts from CSV
[**list_contact_lists**](ContactListsApi.md#list_contact_lists) | **GET** /v1/contact-lists | List contact lists
[**query_contact_list**](ContactListsApi.md#query_contact_list) | **POST** /v1/contact-lists/{list_id}/query | Query contact list
[**update_contact**](ContactListsApi.md#update_contact) | **PATCH** /v1/contact-lists/{list_id}/contacts/{contact_id} | Update contact


# **add_contact**
> AddContact201Response add_contact(list_id, add_contact_request)

Add contact to list

Add a single contact to a contact list.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.add_contact201_response import AddContact201Response
from mailodds.models.add_contact_request import AddContactRequest
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
    api_instance = mailodds.ContactListsApi(api_client)
    list_id = 'list_id_example' # str | 
    add_contact_request = mailodds.AddContactRequest() # AddContactRequest | 

    try:
        # Add contact to list
        api_response = api_instance.add_contact(list_id, add_contact_request)
        print("The response of ContactListsApi->add_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactListsApi->add_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **add_contact_request** | [**AddContactRequest**](AddContactRequest.md)|  | 

### Return type

[**AddContact201Response**](AddContact201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Contact added |  -  |
**404** | Resource not found |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = mailodds.ContactListsApi(api_client)
    list_id = 'list_id_example' # str | 
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
 **list_id** | **str**|  | 
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
**404** | Resource not found |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

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
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> DeletePolicyRule200Response delete_contact(list_id, contact_id)

Delete contact

Remove a single contact from a contact list.

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
    api_instance = mailodds.ContactListsApi(api_client)
    list_id = 'list_id_example' # str | 
    contact_id = 'contact_id_example' # str | 

    try:
        # Delete contact
        api_response = api_instance.delete_contact(list_id, contact_id)
        print("The response of ContactListsApi->delete_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactListsApi->delete_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **contact_id** | **str**|  | 

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
**200** | Contact deleted |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

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
    api_instance = mailodds.ContactListsApi(api_client)
    list_id = 'list_id_example' # str | 

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
 **list_id** | **str**|  | 

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
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_contact_list**
> str export_contact_list(list_id)

Export contact list

Export a contact list as CSV.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
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
    api_instance = mailodds.ContactListsApi(api_client)
    list_id = 'list_id_example' # str | 

    try:
        # Export contact list
        api_response = api_instance.export_contact_list(list_id)
        print("The response of ContactListsApi->export_contact_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactListsApi->export_contact_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CSV export |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

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
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_contact_list**
> ImportContactList200Response import_contact_list(list_id, file, column_mapping=column_mapping, consent_source=consent_source, tags=tags)

Import contacts from CSV

Import contacts into a list from a CSV file (max 10MB).

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.import_contact_list200_response import ImportContactList200Response
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
    api_instance = mailodds.ContactListsApi(api_client)
    list_id = 'list_id_example' # str | 
    file = None # bytearray | CSV file (max 10MB)
    column_mapping = 'column_mapping_example' # str | JSON mapping of CSV columns to contact fields (optional)
    consent_source = 'consent_source_example' # str | Source of consent for imported contacts (optional)
    tags = 'tags_example' # str | JSON array of tags to apply (optional)

    try:
        # Import contacts from CSV
        api_response = api_instance.import_contact_list(list_id, file, column_mapping=column_mapping, consent_source=consent_source, tags=tags)
        print("The response of ContactListsApi->import_contact_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactListsApi->import_contact_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **file** | **bytearray**| CSV file (max 10MB) | 
 **column_mapping** | **str**| JSON mapping of CSV columns to contact fields | [optional] 
 **consent_source** | **str**| Source of consent for imported contacts | [optional] 
 **tags** | **str**| JSON array of tags to apply | [optional] 

### Return type

[**ImportContactList200Response**](ImportContactList200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Import results |  -  |
**404** | Resource not found |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

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
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

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
    api_instance = mailodds.ContactListsApi(api_client)
    list_id = 'list_id_example' # str | 
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
 **list_id** | **str**|  | 
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
**404** | Resource not found |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> AddContact201Response update_contact(list_id, contact_id, update_contact_request)

Update contact

Update a single contact in a contact list.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.add_contact201_response import AddContact201Response
from mailodds.models.update_contact_request import UpdateContactRequest
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
    api_instance = mailodds.ContactListsApi(api_client)
    list_id = 'list_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    update_contact_request = mailodds.UpdateContactRequest() # UpdateContactRequest | 

    try:
        # Update contact
        api_response = api_instance.update_contact(list_id, contact_id, update_contact_request)
        print("The response of ContactListsApi->update_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactListsApi->update_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **update_contact_request** | [**UpdateContactRequest**](UpdateContactRequest.md)|  | 

### Return type

[**AddContact201Response**](AddContact201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact updated |  -  |
**404** | Resource not found |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

