# CrossReferenceBounces200ResponseCrossReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_bounced** | **int** |  | [optional] 
**matched** | **int** | Bounced emails found in validation logs | [optional] 
**unmatched** | **int** | Bounced emails not in validation logs | [optional] 
**match_rate** | **float** |  | [optional] 
**entries** | [**List[CrossReferenceBounces200ResponseCrossReferenceEntriesInner]**](CrossReferenceBounces200ResponseCrossReferenceEntriesInner.md) |  | [optional] 

## Example

```python
from mailodds.models.cross_reference_bounces200_response_cross_reference import CrossReferenceBounces200ResponseCrossReference

# TODO update the JSON string below
json = "{}"
# create an instance of CrossReferenceBounces200ResponseCrossReference from a JSON string
cross_reference_bounces200_response_cross_reference_instance = CrossReferenceBounces200ResponseCrossReference.from_json(json)
# print the JSON string representation of the object
print(CrossReferenceBounces200ResponseCrossReference.to_json())

# convert the object into a dict
cross_reference_bounces200_response_cross_reference_dict = cross_reference_bounces200_response_cross_reference_instance.to_dict()
# create an instance of CrossReferenceBounces200ResponseCrossReference from a dict
cross_reference_bounces200_response_cross_reference_from_dict = CrossReferenceBounces200ResponseCrossReference.from_dict(cross_reference_bounces200_response_cross_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


