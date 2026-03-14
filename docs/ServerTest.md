# ServerTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Test UUID | [optional] 
**domain** | **str** | Tested domain | [optional] 
**status** | **str** | Test status | [optional] 
**mx_records** | [**List[ServerTestMxRecordsInner]**](ServerTestMxRecordsInner.md) |  | [optional] 
**smtp_check** | [**ServerTestSmtpCheck**](ServerTestSmtpCheck.md) |  | [optional] 
**dns_checks** | [**ServerTestDnsChecks**](ServerTestDnsChecks.md) |  | [optional] 
**score** | **int** | Overall server configuration score (0-100) | [optional] 
**recommendations** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.server_test import ServerTest

# TODO update the JSON string below
json = "{}"
# create an instance of ServerTest from a JSON string
server_test_instance = ServerTest.from_json(json)
# print the JSON string representation of the object
print(ServerTest.to_json())

# convert the object into a dict
server_test_dict = server_test_instance.to_dict()
# create an instance of ServerTest from a dict
server_test_from_dict = ServerTest.from_dict(server_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


