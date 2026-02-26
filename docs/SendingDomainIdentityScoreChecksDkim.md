# SendingDomainIdentityScoreChecksDkim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**score** | **float** |  | [optional] 

## Example

```python
from mailodds.models.sending_domain_identity_score_checks_dkim import SendingDomainIdentityScoreChecksDkim

# TODO update the JSON string below
json = "{}"
# create an instance of SendingDomainIdentityScoreChecksDkim from a JSON string
sending_domain_identity_score_checks_dkim_instance = SendingDomainIdentityScoreChecksDkim.from_json(json)
# print the JSON string representation of the object
print(SendingDomainIdentityScoreChecksDkim.to_json())

# convert the object into a dict
sending_domain_identity_score_checks_dkim_dict = sending_domain_identity_score_checks_dkim_instance.to_dict()
# create an instance of SendingDomainIdentityScoreChecksDkim from a dict
sending_domain_identity_score_checks_dkim_from_dict = SendingDomainIdentityScoreChecksDkim.from_dict(sending_domain_identity_score_checks_dkim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


