# BounceAnalysisResponseAnalysis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Analysis UUID | [optional] 
**domain_id** | **str** |  | [optional] 
**period** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**total_bounces** | **int** |  | [optional] 
**hard_bounces** | **int** |  | [optional] 
**soft_bounces** | **int** |  | [optional] 
**categories** | [**BounceAnalysisResponseAnalysisCategories**](BounceAnalysisResponseAnalysisCategories.md) |  | [optional] 
**top_domains** | [**List[BounceAnalysisResponseAnalysisTopDomainsInner]**](BounceAnalysisResponseAnalysisTopDomainsInner.md) | Top bouncing recipient domains | [optional] 
**recommendations** | **List[str]** | Actionable recommendations to reduce bounces | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.bounce_analysis_response_analysis import BounceAnalysisResponseAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of BounceAnalysisResponseAnalysis from a JSON string
bounce_analysis_response_analysis_instance = BounceAnalysisResponseAnalysis.from_json(json)
# print the JSON string representation of the object
print(BounceAnalysisResponseAnalysis.to_json())

# convert the object into a dict
bounce_analysis_response_analysis_dict = bounce_analysis_response_analysis_instance.to_dict()
# create an instance of BounceAnalysisResponseAnalysis from a dict
bounce_analysis_response_analysis_from_dict = BounceAnalysisResponseAnalysis.from_dict(bounce_analysis_response_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


