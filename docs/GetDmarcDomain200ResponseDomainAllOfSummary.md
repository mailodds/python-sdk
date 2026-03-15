# GetDmarcDomain200ResponseDomainAllOfSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** |  | [optional] 
**report_count** | **int** |  | [optional] 
**source_count** | **int** |  | [optional] 
**total_messages** | **int** |  | [optional] 
**total_pass** | **int** |  | [optional] 
**total_fail** | **int** |  | [optional] 
**pass_rate** | **float** |  | [optional] 

## Example

```python
from mailodds.models.get_dmarc_domain200_response_domain_all_of_summary import GetDmarcDomain200ResponseDomainAllOfSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GetDmarcDomain200ResponseDomainAllOfSummary from a JSON string
get_dmarc_domain200_response_domain_all_of_summary_instance = GetDmarcDomain200ResponseDomainAllOfSummary.from_json(json)
# print the JSON string representation of the object
print(GetDmarcDomain200ResponseDomainAllOfSummary.to_json())

# convert the object into a dict
get_dmarc_domain200_response_domain_all_of_summary_dict = get_dmarc_domain200_response_domain_all_of_summary_instance.to_dict()
# create an instance of GetDmarcDomain200ResponseDomainAllOfSummary from a dict
get_dmarc_domain200_response_domain_all_of_summary_from_dict = GetDmarcDomain200ResponseDomainAllOfSummary.from_dict(get_dmarc_domain200_response_domain_all_of_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


