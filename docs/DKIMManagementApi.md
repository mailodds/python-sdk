# mailodds.DKIMManagementApi

All URIs are relative to *https://api.mailodds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dkim_dns_record**](DKIMManagementApi.md#get_dkim_dns_record) | **GET** /v1/sending-domains/{domain_id}/dkim/dns-record | Get DKIM DNS record
[**rotate_dkim**](DKIMManagementApi.md#rotate_dkim) | **POST** /v1/sending-domains/{domain_id}/dkim/rotate | Rotate DKIM keys


# **get_dkim_dns_record**
> get_dkim_dns_record(domain_id)

Get DKIM DNS record

Retrieve the current DKIM DNS record and selector for a sending domain.

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
    api_instance = mailodds.DKIMManagementApi(api_client)
    domain_id = 'domain_id_example' # str | 

    try:
        # Get DKIM DNS record
        api_instance.get_dkim_dns_record(domain_id)
    except Exception as e:
        print("Exception when calling DKIMManagementApi->get_dkim_dns_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get DKIM DNS record |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_dkim**
> rotate_dkim(domain_id)

Rotate DKIM keys

Generate a new DKIM key pair and rotate the selector for a sending domain.

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
    api_instance = mailodds.DKIMManagementApi(api_client)
    domain_id = 'domain_id_example' # str | 

    try:
        # Rotate DKIM keys
        api_instance.rotate_dkim(domain_id)
    except Exception as e:
        print("Exception when calling DKIMManagementApi->rotate_dkim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rotate DKIM keys |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

