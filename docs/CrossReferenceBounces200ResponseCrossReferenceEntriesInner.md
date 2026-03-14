# CrossReferenceBounces200ResponseCrossReferenceEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**bounce_type** | **str** |  | [optional] 
**bounced_at** | **datetime** |  | [optional] 
**validation_status** | **str** |  | [optional] 
**validated_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.cross_reference_bounces200_response_cross_reference_entries_inner import CrossReferenceBounces200ResponseCrossReferenceEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CrossReferenceBounces200ResponseCrossReferenceEntriesInner from a JSON string
cross_reference_bounces200_response_cross_reference_entries_inner_instance = CrossReferenceBounces200ResponseCrossReferenceEntriesInner.from_json(json)
# print the JSON string representation of the object
print(CrossReferenceBounces200ResponseCrossReferenceEntriesInner.to_json())

# convert the object into a dict
cross_reference_bounces200_response_cross_reference_entries_inner_dict = cross_reference_bounces200_response_cross_reference_entries_inner_instance.to_dict()
# create an instance of CrossReferenceBounces200ResponseCrossReferenceEntriesInner from a dict
cross_reference_bounces200_response_cross_reference_entries_inner_from_dict = CrossReferenceBounces200ResponseCrossReferenceEntriesInner.from_dict(cross_reference_bounces200_response_cross_reference_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


