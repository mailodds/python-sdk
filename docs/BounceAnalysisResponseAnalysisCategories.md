# BounceAnalysisResponseAnalysisCategories

Bounce category breakdown

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invalid_recipient** | **int** |  | [optional] 
**mailbox_full** | **int** |  | [optional] 
**domain_issue** | **int** |  | [optional] 
**policy_rejection** | **int** |  | [optional] 
**content_rejection** | **int** |  | [optional] 
**other** | **int** |  | [optional] 

## Example

```python
from mailodds.models.bounce_analysis_response_analysis_categories import BounceAnalysisResponseAnalysisCategories

# TODO update the JSON string below
json = "{}"
# create an instance of BounceAnalysisResponseAnalysisCategories from a JSON string
bounce_analysis_response_analysis_categories_instance = BounceAnalysisResponseAnalysisCategories.from_json(json)
# print the JSON string representation of the object
print(BounceAnalysisResponseAnalysisCategories.to_json())

# convert the object into a dict
bounce_analysis_response_analysis_categories_dict = bounce_analysis_response_analysis_categories_instance.to_dict()
# create an instance of BounceAnalysisResponseAnalysisCategories from a dict
bounce_analysis_response_analysis_categories_from_dict = BounceAnalysisResponseAnalysisCategories.from_dict(bounce_analysis_response_analysis_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


