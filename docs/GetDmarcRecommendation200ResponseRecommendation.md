# GetDmarcRecommendation200ResponseRecommendation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_policy** | **str** | Current DMARC policy (none, quarantine, reject) | [optional] 
**recommended_policy** | **str** | Recommended DMARC policy | [optional] 
**confidence** | **float** | Confidence level (0-1) | [optional] 
**reasons** | **List[str]** | Reasons for the recommendation | [optional] 
**ready_to_upgrade** | **bool** | Whether it is safe to upgrade | [optional] 

## Example

```python
from mailodds.models.get_dmarc_recommendation200_response_recommendation import GetDmarcRecommendation200ResponseRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of GetDmarcRecommendation200ResponseRecommendation from a JSON string
get_dmarc_recommendation200_response_recommendation_instance = GetDmarcRecommendation200ResponseRecommendation.from_json(json)
# print the JSON string representation of the object
print(GetDmarcRecommendation200ResponseRecommendation.to_json())

# convert the object into a dict
get_dmarc_recommendation200_response_recommendation_dict = get_dmarc_recommendation200_response_recommendation_instance.to_dict()
# create an instance of GetDmarcRecommendation200ResponseRecommendation from a dict
get_dmarc_recommendation200_response_recommendation_from_dict = GetDmarcRecommendation200ResponseRecommendation.from_dict(get_dmarc_recommendation200_response_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


