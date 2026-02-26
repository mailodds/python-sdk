# SendingDomainIdentityScoreChecks

Individual check results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dkim** | [**SendingDomainIdentityScoreChecksDkim**](SendingDomainIdentityScoreChecksDkim.md) |  | [optional] 
**spf** | [**SendingDomainIdentityScoreChecksDkim**](SendingDomainIdentityScoreChecksDkim.md) |  | [optional] 
**dmarc** | [**SendingDomainIdentityScoreChecksDmarc**](SendingDomainIdentityScoreChecksDmarc.md) |  | [optional] 
**mx** | [**SendingDomainIdentityScoreChecksDkim**](SendingDomainIdentityScoreChecksDkim.md) |  | [optional] 
**return_path** | [**SendingDomainIdentityScoreChecksDkim**](SendingDomainIdentityScoreChecksDkim.md) |  | [optional] 

## Example

```python
from mailodds.models.sending_domain_identity_score_checks import SendingDomainIdentityScoreChecks

# TODO update the JSON string below
json = "{}"
# create an instance of SendingDomainIdentityScoreChecks from a JSON string
sending_domain_identity_score_checks_instance = SendingDomainIdentityScoreChecks.from_json(json)
# print the JSON string representation of the object
print(SendingDomainIdentityScoreChecks.to_json())

# convert the object into a dict
sending_domain_identity_score_checks_dict = sending_domain_identity_score_checks_instance.to_dict()
# create an instance of SendingDomainIdentityScoreChecks from a dict
sending_domain_identity_score_checks_from_dict = SendingDomainIdentityScoreChecks.from_dict(sending_domain_identity_score_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


