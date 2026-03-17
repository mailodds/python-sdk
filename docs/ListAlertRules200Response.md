# ListAlertRules200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**rules** | [**List[AlertRule]**](AlertRule.md) |  | [optional] 

## Example

```python
from mailodds.models.list_alert_rules200_response import ListAlertRules200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAlertRules200Response from a JSON string
list_alert_rules200_response_instance = ListAlertRules200Response.from_json(json)
# print the JSON string representation of the object
print(ListAlertRules200Response.to_json())

# convert the object into a dict
list_alert_rules200_response_dict = list_alert_rules200_response_instance.to_dict()
# create an instance of ListAlertRules200Response from a dict
list_alert_rules200_response_from_dict = ListAlertRules200Response.from_dict(list_alert_rules200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


