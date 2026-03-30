# UpdateAlertRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | [optional] 
**threshold** | **float** |  | [optional] 
**channel** | **str** |  | [optional] 
**window_minutes** | **int** | Evaluation window in minutes (15, 60, 1440, or 2880) | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from mailodds.models.update_alert_rule_request import UpdateAlertRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAlertRuleRequest from a JSON string
update_alert_rule_request_instance = UpdateAlertRuleRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAlertRuleRequest.to_json())

# convert the object into a dict
update_alert_rule_request_dict = update_alert_rule_request_instance.to_dict()
# create an instance of UpdateAlertRuleRequest from a dict
update_alert_rule_request_from_dict = UpdateAlertRuleRequest.from_dict(update_alert_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


