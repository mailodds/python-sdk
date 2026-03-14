# SpamCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Spam check UUID | [optional] 
**from_domain** | **str** |  | [optional] 
**score** | **float** | Overall spam score (0-10, lower is better) | [optional] 
**verdict** | **str** | Overall verdict | [optional] 
**checks** | [**SpamCheckChecks**](SpamCheckChecks.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.spam_check import SpamCheck

# TODO update the JSON string below
json = "{}"
# create an instance of SpamCheck from a JSON string
spam_check_instance = SpamCheck.from_json(json)
# print the JSON string representation of the object
print(SpamCheck.to_json())

# convert the object into a dict
spam_check_dict = spam_check_instance.to_dict()
# create an instance of SpamCheck from a dict
spam_check_from_dict = SpamCheck.from_dict(spam_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


