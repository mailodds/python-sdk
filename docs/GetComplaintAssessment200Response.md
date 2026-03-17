# GetComplaintAssessment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**complaint_rate** | **float** |  | [optional] 
**risk_level** | **str** |  | [optional] 
**total_complaints** | **int** |  | [optional] 
**total_sent** | **int** |  | [optional] 

## Example

```python
from mailodds.models.get_complaint_assessment200_response import GetComplaintAssessment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetComplaintAssessment200Response from a JSON string
get_complaint_assessment200_response_instance = GetComplaintAssessment200Response.from_json(json)
# print the JSON string representation of the object
print(GetComplaintAssessment200Response.to_json())

# convert the object into a dict
get_complaint_assessment200_response_dict = get_complaint_assessment200_response_instance.to_dict()
# create an instance of GetComplaintAssessment200Response from a dict
get_complaint_assessment200_response_from_dict = GetComplaintAssessment200Response.from_dict(get_complaint_assessment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


