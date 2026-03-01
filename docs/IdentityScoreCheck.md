# IdentityScoreCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Check status (e.g. verified, pending, missing) | 
**points** | **int** | Points earned for this check | 
**max_points** | **int** | Maximum points available for this check | 
**verified_at** | **datetime** | When the check was last verified | [optional] 

## Example

```python
from mailodds.models.identity_score_check import IdentityScoreCheck

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityScoreCheck from a JSON string
identity_score_check_instance = IdentityScoreCheck.from_json(json)
# print the JSON string representation of the object
print(IdentityScoreCheck.to_json())

# convert the object into a dict
identity_score_check_dict = identity_score_check_instance.to_dict()
# create an instance of IdentityScoreCheck from a dict
identity_score_check_from_dict = IdentityScoreCheck.from_dict(identity_score_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


