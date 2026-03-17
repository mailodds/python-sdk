# GetReputationTimeline200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**timeline** | **List[object]** |  | [optional] 

## Example

```python
from mailodds.models.get_reputation_timeline200_response import GetReputationTimeline200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetReputationTimeline200Response from a JSON string
get_reputation_timeline200_response_instance = GetReputationTimeline200Response.from_json(json)
# print the JSON string representation of the object
print(GetReputationTimeline200Response.to_json())

# convert the object into a dict
get_reputation_timeline200_response_dict = get_reputation_timeline200_response_instance.to_dict()
# create an instance of GetReputationTimeline200Response from a dict
get_reputation_timeline200_response_from_dict = GetReputationTimeline200Response.from_dict(get_reputation_timeline200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


