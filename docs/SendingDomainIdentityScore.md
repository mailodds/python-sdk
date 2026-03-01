# SendingDomainIdentityScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** | Total points earned across all checks | 
**max_score** | **int** | Maximum possible score (100) | 
**percentage** | **int** | Score as percentage (same as score since max is 100) | 
**breakdown** | [**SendingDomainIdentityScoreBreakdown**](SendingDomainIdentityScoreBreakdown.md) |  | 
**grade** | **str** | Letter grade (A+, A, B, C, D, F) | 

## Example

```python
from mailodds.models.sending_domain_identity_score import SendingDomainIdentityScore

# TODO update the JSON string below
json = "{}"
# create an instance of SendingDomainIdentityScore from a JSON string
sending_domain_identity_score_instance = SendingDomainIdentityScore.from_json(json)
# print the JSON string representation of the object
print(SendingDomainIdentityScore.to_json())

# convert the object into a dict
sending_domain_identity_score_dict = sending_domain_identity_score_instance.to_dict()
# create an instance of SendingDomainIdentityScore from a dict
sending_domain_identity_score_from_dict = SendingDomainIdentityScore.from_dict(sending_domain_identity_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


