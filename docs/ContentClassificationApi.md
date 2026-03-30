# mailodds.ContentClassificationApi

All URIs are relative to *https://api.mailodds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classify_content**](ContentClassificationApi.md#classify_content) | **POST** /v1/content-check | Classify email content


# **classify_content**
> ClassifyContent200Response classify_content(classify_content_request)

Classify email content

Run LLM-powered content analysis on email content. Detects spam signals, compliance issues, and content quality. Provide either subject+html_body or raw content text.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.classify_content200_response import ClassifyContent200Response
from mailodds.models.classify_content_request import ClassifyContentRequest
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
    api_instance = mailodds.ContentClassificationApi(api_client)
    classify_content_request = mailodds.ClassifyContentRequest() # ClassifyContentRequest | 

    try:
        # Classify email content
        api_response = api_instance.classify_content(classify_content_request)
        print("The response of ContentClassificationApi->classify_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentClassificationApi->classify_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classify_content_request** | [**ClassifyContentRequest**](ClassifyContentRequest.md)|  | 

### Return type

[**ClassifyContent200Response**](ClassifyContent200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Content classification result |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

