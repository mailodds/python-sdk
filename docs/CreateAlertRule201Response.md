# CreateAlertRule201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**rule** | [**AlertRule**](AlertRule.md) |  | [optional] 

## Example

```python
from mailodds.models.create_alert_rule201_response import CreateAlertRule201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlertRule201Response from a JSON string
create_alert_rule201_response_instance = CreateAlertRule201Response.from_json(json)
# print the JSON string representation of the object
print(CreateAlertRule201Response.to_json())

# convert the object into a dict
create_alert_rule201_response_dict = create_alert_rule201_response_instance.to_dict()
# create an instance of CreateAlertRule201Response from a dict
create_alert_rule201_response_from_dict = CreateAlertRule201Response.from_dict(create_alert_rule201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


