# TelemetrySummaryTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validations** | **int** | Total validations in window | [optional] 
**credits_used** | **int** | Credits consumed | [optional] 

## Example

```python
from mailodds.models.telemetry_summary_totals import TelemetrySummaryTotals

# TODO update the JSON string below
json = "{}"
# create an instance of TelemetrySummaryTotals from a JSON string
telemetry_summary_totals_instance = TelemetrySummaryTotals.from_json(json)
# print the JSON string representation of the object
print(TelemetrySummaryTotals.to_json())

# convert the object into a dict
telemetry_summary_totals_dict = telemetry_summary_totals_instance.to_dict()
# create an instance of TelemetrySummaryTotals from a dict
telemetry_summary_totals_from_dict = TelemetrySummaryTotals.from_dict(telemetry_summary_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


