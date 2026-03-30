# mailodds.AgentControlPlaneApi

All URIs are relative to *https://api.mailodds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mcp_capabilities**](AgentControlPlaneApi.md#get_mcp_capabilities) | **GET** /v1/mcp/capabilities | Get MCP capabilities


# **get_mcp_capabilities**
> McpCapabilities get_mcp_capabilities()

Get MCP capabilities

Returns a static capability manifest listing all MCP tools organized by pillar. Used by AI agents for tool discovery and scope-based self-correction.

### Example


```python
import mailodds
from mailodds.models.mcp_capabilities import McpCapabilities
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
    api_instance = mailodds.AgentControlPlaneApi(api_client)

    try:
        # Get MCP capabilities
        api_response = api_instance.get_mcp_capabilities()
        print("The response of AgentControlPlaneApi->get_mcp_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlPlaneApi->get_mcp_capabilities: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**McpCapabilities**](McpCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MCP capability manifest |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

