# McpCapabilities

MCP capability manifest for AI agent discovery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**server_name** | **str** |  | [optional] 
**tool_count** | **int** | Total number of available tools | [optional] 
**pillars** | [**List[McpCapabilitiesPillarsInner]**](McpCapabilitiesPillarsInner.md) |  | [optional] 
**supported_transports** | **List[str]** |  | [optional] 
**auth_required** | **bool** |  | [optional] 

## Example

```python
from mailodds.models.mcp_capabilities import McpCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of McpCapabilities from a JSON string
mcp_capabilities_instance = McpCapabilities.from_json(json)
# print the JSON string representation of the object
print(McpCapabilities.to_json())

# convert the object into a dict
mcp_capabilities_dict = mcp_capabilities_instance.to_dict()
# create an instance of McpCapabilities from a dict
mcp_capabilities_from_dict = McpCapabilities.from_dict(mcp_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


