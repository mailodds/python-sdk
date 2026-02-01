# TelemetrySummary

Validation metrics for building dashboards and monitoring.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**window** | **str** |  | [optional] 
**generated_at** | **datetime** |  | [optional] 
**timezone** | **str** |  | [optional] 
**totals** | [**TelemetrySummaryTotals**](TelemetrySummaryTotals.md) |  | [optional] 
**rates** | [**TelemetrySummaryRates**](TelemetrySummaryRates.md) |  | [optional] 
**top_reasons** | [**List[TelemetrySummaryTopReasonsInner]**](TelemetrySummaryTopReasonsInner.md) | Top rejection/status reasons | [optional] 
**top_domains** | [**List[TelemetrySummaryTopDomainsInner]**](TelemetrySummaryTopDomainsInner.md) | Top domains by volume | [optional] 

## Example

```python
from mailodds.models.telemetry_summary import TelemetrySummary

# TODO update the JSON string below
json = "{}"
# create an instance of TelemetrySummary from a JSON string
telemetry_summary_instance = TelemetrySummary.from_json(json)
# print the JSON string representation of the object
print(TelemetrySummary.to_json())

# convert the object into a dict
telemetry_summary_dict = telemetry_summary_instance.to_dict()
# create an instance of TelemetrySummary from a dict
telemetry_summary_from_dict = TelemetrySummary.from_dict(telemetry_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


