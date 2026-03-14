# SpamCheckChecks

Individual check results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_reputation** | **object** |  | [optional] 
**link_safety** | **object** |  | [optional] 
**subject_analysis** | **object** |  | [optional] 

## Example

```python
from mailodds.models.spam_check_checks import SpamCheckChecks

# TODO update the JSON string below
json = "{}"
# create an instance of SpamCheckChecks from a JSON string
spam_check_checks_instance = SpamCheckChecks.from_json(json)
# print the JSON string representation of the object
print(SpamCheckChecks.to_json())

# convert the object into a dict
spam_check_checks_dict = spam_check_checks_instance.to_dict()
# create an instance of SpamCheckChecks from a dict
spam_check_checks_from_dict = SpamCheckChecks.from_dict(spam_check_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


