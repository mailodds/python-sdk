# TelemetrySummaryRates

Status distribution as decimals (0-1)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deliverable** | **float** | Rate of valid + catch_all emails | [optional] 
**reject** | **float** | Rate of invalid + do_not_mail emails | [optional] 
**unknown** | **float** | Rate of unknown status | [optional] 
**suppressed** | **float** | Rate of suppressed emails | [optional] 

## Example

```python
from mailodds.models.telemetry_summary_rates import TelemetrySummaryRates

# TODO update the JSON string below
json = "{}"
# create an instance of TelemetrySummaryRates from a JSON string
telemetry_summary_rates_instance = TelemetrySummaryRates.from_json(json)
# print the JSON string representation of the object
print(TelemetrySummaryRates.to_json())

# convert the object into a dict
telemetry_summary_rates_dict = telemetry_summary_rates_instance.to_dict()
# create an instance of TelemetrySummaryRates from a dict
telemetry_summary_rates_from_dict = TelemetrySummaryRates.from_dict(telemetry_summary_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


