# McpCapabilitiesPillarsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**tool_count** | **int** |  | [optional] 
**tools** | [**List[McpCapabilitiesPillarsInnerToolsInner]**](McpCapabilitiesPillarsInnerToolsInner.md) |  | [optional] 

## Example

```python
from mailodds.models.mcp_capabilities_pillars_inner import McpCapabilitiesPillarsInner

# TODO update the JSON string below
json = "{}"
# create an instance of McpCapabilitiesPillarsInner from a JSON string
mcp_capabilities_pillars_inner_instance = McpCapabilitiesPillarsInner.from_json(json)
# print the JSON string representation of the object
print(McpCapabilitiesPillarsInner.to_json())

# convert the object into a dict
mcp_capabilities_pillars_inner_dict = mcp_capabilities_pillars_inner_instance.to_dict()
# create an instance of McpCapabilitiesPillarsInner from a dict
mcp_capabilities_pillars_inner_from_dict = McpCapabilitiesPillarsInner.from_dict(mcp_capabilities_pillars_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


