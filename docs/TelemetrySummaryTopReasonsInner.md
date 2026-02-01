# TelemetrySummaryTopReasonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from mailodds.models.telemetry_summary_top_reasons_inner import TelemetrySummaryTopReasonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TelemetrySummaryTopReasonsInner from a JSON string
telemetry_summary_top_reasons_inner_instance = TelemetrySummaryTopReasonsInner.from_json(json)
# print the JSON string representation of the object
print(TelemetrySummaryTopReasonsInner.to_json())

# convert the object into a dict
telemetry_summary_top_reasons_inner_dict = telemetry_summary_top_reasons_inner_instance.to_dict()
# create an instance of TelemetrySummaryTopReasonsInner from a dict
telemetry_summary_top_reasons_inner_from_dict = TelemetrySummaryTopReasonsInner.from_dict(telemetry_summary_top_reasons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


