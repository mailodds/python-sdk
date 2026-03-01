# SendingDomainIdentityScoreBreakdown

Per-check scoring breakdown

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dkim** | [**IdentityScoreCheck**](IdentityScoreCheck.md) |  | [optional] 
**spf** | [**IdentityScoreCheck**](IdentityScoreCheck.md) |  | [optional] 
**dmarc** | [**IdentityScoreCheck**](IdentityScoreCheck.md) |  | [optional] 
**mx** | [**IdentityScoreCheck**](IdentityScoreCheck.md) |  | [optional] 
**return_path** | [**IdentityScoreCheck**](IdentityScoreCheck.md) |  | [optional] 
**bimi** | [**IdentityScoreCheck**](IdentityScoreCheck.md) |  | [optional] 

## Example

```python
from mailodds.models.sending_domain_identity_score_breakdown import SendingDomainIdentityScoreBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of SendingDomainIdentityScoreBreakdown from a JSON string
sending_domain_identity_score_breakdown_instance = SendingDomainIdentityScoreBreakdown.from_json(json)
# print the JSON string representation of the object
print(SendingDomainIdentityScoreBreakdown.to_json())

# convert the object into a dict
sending_domain_identity_score_breakdown_dict = sending_domain_identity_score_breakdown_instance.to_dict()
# create an instance of SendingDomainIdentityScoreBreakdown from a dict
sending_domain_identity_score_breakdown_from_dict = SendingDomainIdentityScoreBreakdown.from_dict(sending_domain_identity_score_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


