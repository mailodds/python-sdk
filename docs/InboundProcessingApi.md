# mailodds.InboundProcessingApi

All URIs are relative to *https://api.mailodds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**correct_inbound_message**](InboundProcessingApi.md#correct_inbound_message) | **PATCH** /v1/inbound-messages/{message_id}/correction | Correct inbound message classification
[**get_bounce_stats**](InboundProcessingApi.md#get_bounce_stats) | **GET** /v1/bounce-stats | Get bounce statistics
[**get_bounce_stats_summary**](InboundProcessingApi.md#get_bounce_stats_summary) | **GET** /v1/bounce-stats/summary | Get bounce statistics summary
[**get_complaint_assessment**](InboundProcessingApi.md#get_complaint_assessment) | **GET** /v1/complaint-assessment | Get complaint assessment
[**get_inbound_message**](InboundProcessingApi.md#get_inbound_message) | **GET** /v1/inbound-messages/{message_id} | Get inbound message
[**list_inbound_messages**](InboundProcessingApi.md#list_inbound_messages) | **GET** /v1/inbound-messages | List inbound messages


# **correct_inbound_message**
> GetInboundMessage200Response correct_inbound_message(message_id, correct_inbound_message_request)

Correct inbound message classification

Submit a human correction for an inbound message classification. Requires Pro+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.correct_inbound_message_request import CorrectInboundMessageRequest
from mailodds.models.get_inbound_message200_response import GetInboundMessage200Response
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
    api_instance = mailodds.InboundProcessingApi(api_client)
    message_id = 'message_id_example' # str | 
    correct_inbound_message_request = mailodds.CorrectInboundMessageRequest() # CorrectInboundMessageRequest | 

    try:
        # Correct inbound message classification
        api_response = api_instance.correct_inbound_message(message_id, correct_inbound_message_request)
        print("The response of InboundProcessingApi->correct_inbound_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundProcessingApi->correct_inbound_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**|  | 
 **correct_inbound_message_request** | [**CorrectInboundMessageRequest**](CorrectInboundMessageRequest.md)|  | 

### Return type

[**GetInboundMessage200Response**](GetInboundMessage200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message updated with correction |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**404** | Resource not found |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bounce_stats**
> GetBounceStats200Response get_bounce_stats(domain_id=domain_id, period=period, group_by=group_by)

Get bounce statistics

Get bounce and complaint statistics grouped by time period. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_bounce_stats200_response import GetBounceStats200Response
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
    api_instance = mailodds.InboundProcessingApi(api_client)
    domain_id = 'domain_id_example' # str | Filter by sending domain ID (optional)
    period = 7d # str | Time period (optional) (default to 7d)
    group_by = day # str | Grouping interval (optional) (default to day)

    try:
        # Get bounce statistics
        api_response = api_instance.get_bounce_stats(domain_id=domain_id, period=period, group_by=group_by)
        print("The response of InboundProcessingApi->get_bounce_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundProcessingApi->get_bounce_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Filter by sending domain ID | [optional] 
 **period** | **str**| Time period | [optional] [default to 7d]
 **group_by** | **str**| Grouping interval | [optional] [default to day]

### Return type

[**GetBounceStats200Response**](GetBounceStats200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bounce statistics |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bounce_stats_summary**
> GetBounceStatsSummary200Response get_bounce_stats_summary(domain_id=domain_id, period=period)

Get bounce statistics summary

Get aggregated bounce and complaint statistics. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_bounce_stats_summary200_response import GetBounceStatsSummary200Response
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
    api_instance = mailodds.InboundProcessingApi(api_client)
    domain_id = 'domain_id_example' # str | Filter by sending domain ID (optional)
    period = 30d # str | Time period (optional) (default to 30d)

    try:
        # Get bounce statistics summary
        api_response = api_instance.get_bounce_stats_summary(domain_id=domain_id, period=period)
        print("The response of InboundProcessingApi->get_bounce_stats_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundProcessingApi->get_bounce_stats_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Filter by sending domain ID | [optional] 
 **period** | **str**| Time period | [optional] [default to 30d]

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
**200** | Bounce statistics summary |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_complaint_assessment**
> GetComplaintAssessment200Response get_complaint_assessment(domain_id=domain_id, period=period)

Get complaint assessment

Assess complaint risk based on recent inbound data. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_complaint_assessment200_response import GetComplaintAssessment200Response
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
    api_instance = mailodds.InboundProcessingApi(api_client)
    domain_id = 'domain_id_example' # str | Filter by sending domain ID (optional)
    period = 30d # str | Time period (optional) (default to 30d)

    try:
        # Get complaint assessment
        api_response = api_instance.get_complaint_assessment(domain_id=domain_id, period=period)
        print("The response of InboundProcessingApi->get_complaint_assessment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundProcessingApi->get_complaint_assessment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Filter by sending domain ID | [optional] 
 **period** | **str**| Time period | [optional] [default to 30d]

### Return type

[**GetComplaintAssessment200Response**](GetComplaintAssessment200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complaint assessment |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_message**
> GetInboundMessage200Response get_inbound_message(message_id)

Get inbound message

Get a single inbound message with full body content. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_inbound_message200_response import GetInboundMessage200Response
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
    api_instance = mailodds.InboundProcessingApi(api_client)
    message_id = 'message_id_example' # str | 

    try:
        # Get inbound message
        api_response = api_instance.get_inbound_message(message_id)
        print("The response of InboundProcessingApi->get_inbound_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundProcessingApi->get_inbound_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**|  | 

### Return type

[**GetInboundMessage200Response**](GetInboundMessage200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbound message details |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inbound_messages**
> ListInboundMessages200Response list_inbound_messages(category=category, domain_id=domain_id, since=since, until=until, is_read=is_read, recipient=recipient, search=search, page=page, per_page=per_page)

List inbound messages

List inbound messages (bounces, complaints, replies, OOO). Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.list_inbound_messages200_response import ListInboundMessages200Response
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
    api_instance = mailodds.InboundProcessingApi(api_client)
    category = 'category_example' # str | Filter by category (optional)
    domain_id = 'domain_id_example' # str | Filter by sending domain ID (optional)
    since = '2013-10-20T19:20:30+01:00' # datetime | Start date (ISO 8601) (optional)
    until = '2013-10-20T19:20:30+01:00' # datetime | End date (ISO 8601) (optional)
    is_read = True # bool | Filter by read status (optional)
    recipient = 'recipient_example' # str | Filter by original recipient (optional)
    search = 'search_example' # str | Search in subject and body (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = 50 # int |  (optional) (default to 50)

    try:
        # List inbound messages
        api_response = api_instance.list_inbound_messages(category=category, domain_id=domain_id, since=since, until=until, is_read=is_read, recipient=recipient, search=search, page=page, per_page=per_page)
        print("The response of InboundProcessingApi->list_inbound_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundProcessingApi->list_inbound_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Filter by category | [optional] 
 **domain_id** | **str**| Filter by sending domain ID | [optional] 
 **since** | **datetime**| Start date (ISO 8601) | [optional] 
 **until** | **datetime**| End date (ISO 8601) | [optional] 
 **is_read** | **bool**| Filter by read status | [optional] 
 **recipient** | **str**| Filter by original recipient | [optional] 
 **search** | **str**| Search in subject and body | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 50]

### Return type

[**ListInboundMessages200Response**](ListInboundMessages200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of inbound messages |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

