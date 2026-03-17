# CreateBounceAnalysisRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Bounce log text to analyze. Identifies patterns, categorizes bounce types, and provides remediation recommendations. | 
**name** | **str** | Optional name for this bounce analysis | [optional] 

## Example

```python
from mailodds.models.create_bounce_analysis_request import CreateBounceAnalysisRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBounceAnalysisRequest from a JSON string
create_bounce_analysis_request_instance = CreateBounceAnalysisRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBounceAnalysisRequest.to_json())

# convert the object into a dict
create_bounce_analysis_request_dict = create_bounce_analysis_request_instance.to_dict()
# create an instance of CreateBounceAnalysisRequest from a dict
create_bounce_analysis_request_from_dict = CreateBounceAnalysisRequest.from_dict(create_bounce_analysis_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


