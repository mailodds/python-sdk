# SendingDomainIdentityScoreChecksDmarc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**policy** | **str** |  | [optional] 

## Example

```python
from mailodds.models.sending_domain_identity_score_checks_dmarc import SendingDomainIdentityScoreChecksDmarc

# TODO update the JSON string below
json = "{}"
# create an instance of SendingDomainIdentityScoreChecksDmarc from a JSON string
sending_domain_identity_score_checks_dmarc_instance = SendingDomainIdentityScoreChecksDmarc.from_json(json)
# print the JSON string representation of the object
print(SendingDomainIdentityScoreChecksDmarc.to_json())

# convert the object into a dict
sending_domain_identity_score_checks_dmarc_dict = sending_domain_identity_score_checks_dmarc_instance.to_dict()
# create an instance of SendingDomainIdentityScoreChecksDmarc from a dict
sending_domain_identity_score_checks_dmarc_from_dict = SendingDomainIdentityScoreChecksDmarc.from_dict(sending_domain_identity_score_checks_dmarc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


