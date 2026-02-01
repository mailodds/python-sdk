# TelemetrySummaryTopDomainsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**volume** | **int** |  | [optional] 
**deliverable** | **float** |  | [optional] 
**reject** | **float** |  | [optional] 
**unknown** | **float** |  | [optional] 
**catch_all** | **float** |  | [optional] 

## Example

```python
from mailodds.models.telemetry_summary_top_domains_inner import TelemetrySummaryTopDomainsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TelemetrySummaryTopDomainsInner from a JSON string
telemetry_summary_top_domains_inner_instance = TelemetrySummaryTopDomainsInner.from_json(json)
# print the JSON string representation of the object
print(TelemetrySummaryTopDomainsInner.to_json())

# convert the object into a dict
telemetry_summary_top_domains_inner_dict = telemetry_summary_top_domains_inner_instance.to_dict()
# create an instance of TelemetrySummaryTopDomainsInner from a dict
telemetry_summary_top_domains_inner_from_dict = TelemetrySummaryTopDomainsInner.from_dict(telemetry_summary_top_domains_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


