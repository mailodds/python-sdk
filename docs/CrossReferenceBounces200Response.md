# CrossReferenceBounces200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**cross_reference** | [**CrossReferenceBounces200ResponseCrossReference**](CrossReferenceBounces200ResponseCrossReference.md) |  | [optional] 

## Example

```python
from mailodds.models.cross_reference_bounces200_response import CrossReferenceBounces200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CrossReferenceBounces200Response from a JSON string
cross_reference_bounces200_response_instance = CrossReferenceBounces200Response.from_json(json)
# print the JSON string representation of the object
print(CrossReferenceBounces200Response.to_json())

# convert the object into a dict
cross_reference_bounces200_response_dict = cross_reference_bounces200_response_instance.to_dict()
# create an instance of CrossReferenceBounces200Response from a dict
cross_reference_bounces200_response_from_dict = CrossReferenceBounces200Response.from_dict(cross_reference_bounces200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


