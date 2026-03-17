# GetBounceStatsSummary200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**summary** | **object** |  | [optional] 

## Example

```python
from mailodds.models.get_bounce_stats_summary200_response import GetBounceStatsSummary200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBounceStatsSummary200Response from a JSON string
get_bounce_stats_summary200_response_instance = GetBounceStatsSummary200Response.from_json(json)
# print the JSON string representation of the object
print(GetBounceStatsSummary200Response.to_json())

# convert the object into a dict
get_bounce_stats_summary200_response_dict = get_bounce_stats_summary200_response_instance.to_dict()
# create an instance of GetBounceStatsSummary200Response from a dict
get_bounce_stats_summary200_response_from_dict = GetBounceStatsSummary200Response.from_dict(get_bounce_stats_summary200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


