# mailodds.EngagementApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_disengaged_contacts**](EngagementApi.md#get_disengaged_contacts) | **GET** /v1/engagement/disengaged | List disengaged contacts
[**get_engagement_score**](EngagementApi.md#get_engagement_score) | **GET** /v1/engagement/score/{email} | Get engagement score
[**get_engagement_summary**](EngagementApi.md#get_engagement_summary) | **GET** /v1/engagement/summary | Get engagement summary
[**suppress_disengaged**](EngagementApi.md#suppress_disengaged) | **POST** /v1/engagement/suppress-disengaged | Suppress disengaged contacts


# **get_disengaged_contacts**
> GetDisengagedContacts200Response get_disengaged_contacts(inactive_days=inactive_days, min_sends=min_sends, domain_id=domain_id, page=page, per_page=per_page)

List disengaged contacts

List contacts that have not engaged within the specified period. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_disengaged_contacts200_response import GetDisengagedContacts200Response
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
    api_instance = mailodds.EngagementApi(api_client)
    inactive_days = 90 # int | Days of inactivity (optional) (default to 90)
    min_sends = 5 # int | Minimum emails sent to qualify (optional) (default to 5)
    domain_id = 'domain_id_example' # str | Filter by sending domain ID (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)

    try:
        # List disengaged contacts
        api_response = api_instance.get_disengaged_contacts(inactive_days=inactive_days, min_sends=min_sends, domain_id=domain_id, page=page, per_page=per_page)
        print("The response of EngagementApi->get_disengaged_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementApi->get_disengaged_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inactive_days** | **int**| Days of inactivity | [optional] [default to 90]
 **min_sends** | **int**| Minimum emails sent to qualify | [optional] [default to 5]
 **domain_id** | **str**| Filter by sending domain ID | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 100]

### Return type

[**GetDisengagedContacts200Response**](GetDisengagedContacts200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of disengaged contacts |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_engagement_score**
> GetEngagementScore200Response get_engagement_score(email)

Get engagement score

Get the engagement score for a specific email address. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_engagement_score200_response import GetEngagementScore200Response
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
    api_instance = mailodds.EngagementApi(api_client)
    email = 'email_example' # str | 

    try:
        # Get engagement score
        api_response = api_instance.get_engagement_score(email)
        print("The response of EngagementApi->get_engagement_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementApi->get_engagement_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**GetEngagementScore200Response**](GetEngagementScore200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Engagement score |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_engagement_summary**
> GetBounceStatsSummary200Response get_engagement_summary(domain_id=domain_id)

Get engagement summary

Get aggregate engagement metrics across all contacts. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_bounce_stats_summary200_response import GetBounceStatsSummary200Response
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
    api_instance = mailodds.EngagementApi(api_client)
    domain_id = 'domain_id_example' # str | Filter by sending domain ID (optional)

    try:
        # Get engagement summary
        api_response = api_instance.get_engagement_summary(domain_id=domain_id)
        print("The response of EngagementApi->get_engagement_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementApi->get_engagement_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Filter by sending domain ID | [optional] 

### Return type

[**GetBounceStatsSummary200Response**](GetBounceStatsSummary200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Engagement summary |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppress_disengaged**
> SuppressDisengaged200Response suppress_disengaged(suppress_disengaged_request)

Suppress disengaged contacts

Add disengaged contacts to the suppression list. Supports dry_run mode. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.suppress_disengaged200_response import SuppressDisengaged200Response
from mailodds.models.suppress_disengaged_request import SuppressDisengagedRequest
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
    api_instance = mailodds.EngagementApi(api_client)
    suppress_disengaged_request = mailodds.SuppressDisengagedRequest() # SuppressDisengagedRequest | 

    try:
        # Suppress disengaged contacts
        api_response = api_instance.suppress_disengaged(suppress_disengaged_request)
        print("The response of EngagementApi->suppress_disengaged:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementApi->suppress_disengaged: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suppress_disengaged_request** | [**SuppressDisengagedRequest**](SuppressDisengagedRequest.md)|  | 

### Return type

[**SuppressDisengaged200Response**](SuppressDisengaged200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suppression result or dry-run preview |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

