# BounceAnalysisResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** | Unique request identifier | [optional] 
**analysis** | [**BounceAnalysisResponseAnalysis**](BounceAnalysisResponseAnalysis.md) |  | [optional] 

## Example

```python
from mailodds.models.bounce_analysis_response import BounceAnalysisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BounceAnalysisResponse from a JSON string
bounce_analysis_response_instance = BounceAnalysisResponse.from_json(json)
# print the JSON string representation of the object
print(BounceAnalysisResponse.to_json())

# convert the object into a dict
bounce_analysis_response_dict = bounce_analysis_response_instance.to_dict()
# create an instance of BounceAnalysisResponse from a dict
bounce_analysis_response_from_dict = BounceAnalysisResponse.from_dict(bounce_analysis_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


