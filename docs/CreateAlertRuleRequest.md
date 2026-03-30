# CreateAlertRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** | Metric to monitor (e.g., bounce_rate, complaint_rate) | 
**threshold** | **float** | Threshold value (0-1, e.g. 0.02 for 2%) | 
**channel** | **str** | Notification channel (e.g., webhook) | 
**window_minutes** | **int** | Evaluation window in minutes (15, 60, 1440, or 2880) | [optional] [default to 60]
**enabled** | **bool** |  | [optional] [default to True]

## Example

```python
from mailodds.models.create_alert_rule_request import CreateAlertRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlertRuleRequest from a JSON string
create_alert_rule_request_instance = CreateAlertRuleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAlertRuleRequest.to_json())

# convert the object into a dict
create_alert_rule_request_dict = create_alert_rule_request_instance.to_dict()
# create an instance of CreateAlertRuleRequest from a dict
create_alert_rule_request_from_dict = CreateAlertRuleRequest.from_dict(create_alert_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


