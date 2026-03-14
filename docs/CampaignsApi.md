# mailodds.CampaignsApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_campaign**](CampaignsApi.md#cancel_campaign) | **POST** /v1/campaigns/{campaign_id}/cancel | Cancel a campaign
[**create_campaign**](CampaignsApi.md#create_campaign) | **POST** /v1/campaigns | Create a campaign
[**create_campaign_variant**](CampaignsApi.md#create_campaign_variant) | **POST** /v1/campaigns/{campaign_id}/variants | Create A/B variant
[**get_campaign**](CampaignsApi.md#get_campaign) | **GET** /v1/campaigns/{campaign_id} | Get campaign with stats
[**list_campaigns**](CampaignsApi.md#list_campaigns) | **GET** /v1/campaigns | List campaigns
[**schedule_campaign**](CampaignsApi.md#schedule_campaign) | **POST** /v1/campaigns/{campaign_id}/schedule | Schedule a campaign
[**send_campaign**](CampaignsApi.md#send_campaign) | **POST** /v1/campaigns/{campaign_id}/send | Send a campaign


# **cancel_campaign**
> CampaignResponse cancel_campaign(campaign_id)

Cancel a campaign

Cancel a scheduled or in-progress campaign. Messages already delivered are not recalled.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.campaign_response import CampaignResponse
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
    api_instance = mailodds.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Campaign UUID

    try:
        # Cancel a campaign
        api_response = api_instance.cancel_campaign(campaign_id)
        print("The response of CampaignsApi->cancel_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->cancel_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign UUID | 

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign cancelled |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_campaign**
> CampaignResponse create_campaign(create_campaign_request)

Create a campaign

Create a new email campaign. Campaigns target a subscriber list and support A/B variant testing.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.campaign_response import CampaignResponse
from mailodds.models.create_campaign_request import CreateCampaignRequest
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
    api_instance = mailodds.CampaignsApi(api_client)
    create_campaign_request = mailodds.CreateCampaignRequest() # CreateCampaignRequest | 

    try:
        # Create a campaign
        api_response = api_instance.create_campaign(create_campaign_request)
        print("The response of CampaignsApi->create_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->create_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_campaign_request** | [**CreateCampaignRequest**](CreateCampaignRequest.md)|  | 

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Campaign created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_campaign_variant**
> CreateCampaignVariant201Response create_campaign_variant(campaign_id, create_variant_request)

Create A/B variant

Add an A/B test variant to a campaign. Each variant has its own subject, body, and traffic weight. The campaign must be in draft status.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_campaign_variant201_response import CreateCampaignVariant201Response
from mailodds.models.create_variant_request import CreateVariantRequest
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
    api_instance = mailodds.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Campaign UUID
    create_variant_request = mailodds.CreateVariantRequest() # CreateVariantRequest | 

    try:
        # Create A/B variant
        api_response = api_instance.create_campaign_variant(campaign_id, create_variant_request)
        print("The response of CampaignsApi->create_campaign_variant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->create_campaign_variant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign UUID | 
 **create_variant_request** | [**CreateVariantRequest**](CreateVariantRequest.md)|  | 

### Return type

[**CreateCampaignVariant201Response**](CreateCampaignVariant201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Variant created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign**
> CampaignResponse get_campaign(campaign_id)

Get campaign with stats

Get a campaign by ID including delivery statistics and engagement metrics.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.campaign_response import CampaignResponse
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
    api_instance = mailodds.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Campaign UUID

    try:
        # Get campaign with stats
        api_response = api_instance.get_campaign(campaign_id)
        print("The response of CampaignsApi->get_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->get_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign UUID | 

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign details with stats |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_campaigns**
> ListCampaigns200Response list_campaigns(page=page, per_page=per_page, status=status)

List campaigns

List all campaigns for the authenticated account with pagination.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.list_campaigns200_response import ListCampaigns200Response
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
    api_instance = mailodds.CampaignsApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    per_page = 25 # int | Items per page (optional) (default to 25)
    status = 'status_example' # str | Filter by campaign status (optional)

    try:
        # List campaigns
        api_response = api_instance.list_campaigns(page=page, per_page=per_page, status=status)
        print("The response of CampaignsApi->list_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->list_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 25]
 **status** | **str**| Filter by campaign status | [optional] 

### Return type

[**ListCampaigns200Response**](ListCampaigns200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of campaigns |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_campaign**
> CampaignResponse schedule_campaign(campaign_id, schedule_campaign_request)

Schedule a campaign

Schedule a campaign for future delivery. Provide a send_at timestamp in ISO 8601 format.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.campaign_response import CampaignResponse
from mailodds.models.schedule_campaign_request import ScheduleCampaignRequest
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
    api_instance = mailodds.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Campaign UUID
    schedule_campaign_request = mailodds.ScheduleCampaignRequest() # ScheduleCampaignRequest | 

    try:
        # Schedule a campaign
        api_response = api_instance.schedule_campaign(campaign_id, schedule_campaign_request)
        print("The response of CampaignsApi->schedule_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->schedule_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign UUID | 
 **schedule_campaign_request** | [**ScheduleCampaignRequest**](ScheduleCampaignRequest.md)|  | 

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign scheduled |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_campaign**
> CampaignResponse send_campaign(campaign_id)

Send a campaign

Begin sending a campaign immediately. The campaign must be in draft status with at least one variant and a target list.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.campaign_response import CampaignResponse
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
    api_instance = mailodds.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Campaign UUID

    try:
        # Send a campaign
        api_response = api_instance.send_campaign(campaign_id)
        print("The response of CampaignsApi->send_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->send_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign UUID | 

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Campaign accepted for sending |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

