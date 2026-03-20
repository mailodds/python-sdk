# mailodds.PixelSettingsApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pixel_settings**](PixelSettingsApi.md#get_pixel_settings) | **GET** /v1/pixel-settings | Get pixel settings
[**update_pixel_settings**](PixelSettingsApi.md#update_pixel_settings) | **PATCH** /v1/pixel-settings | Update pixel settings


# **get_pixel_settings**
> GetPixelSettings200Response get_pixel_settings()

Get pixel settings

Get the web pixel tracking configuration.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_pixel_settings200_response import GetPixelSettings200Response
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
    api_instance = mailodds.PixelSettingsApi(api_client)

    try:
        # Get pixel settings
        api_response = api_instance.get_pixel_settings()
        print("The response of PixelSettingsApi->get_pixel_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PixelSettingsApi->get_pixel_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetPixelSettings200Response**](GetPixelSettings200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pixel settings |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pixel_settings**
> GetPixelSettings200Response update_pixel_settings(update_pixel_settings_request)

Update pixel settings

Update the web pixel subscribe list configuration.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_pixel_settings200_response import GetPixelSettings200Response
from mailodds.models.update_pixel_settings_request import UpdatePixelSettingsRequest
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
    api_instance = mailodds.PixelSettingsApi(api_client)
    update_pixel_settings_request = mailodds.UpdatePixelSettingsRequest() # UpdatePixelSettingsRequest | 

    try:
        # Update pixel settings
        api_response = api_instance.update_pixel_settings(update_pixel_settings_request)
        print("The response of PixelSettingsApi->update_pixel_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PixelSettingsApi->update_pixel_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_pixel_settings_request** | [**UpdatePixelSettingsRequest**](UpdatePixelSettingsRequest.md)|  | 

### Return type

[**GetPixelSettings200Response**](GetPixelSettings200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pixel settings updated |  -  |
**404** | Resource not found |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

