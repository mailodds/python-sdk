# ServerTestSmtpCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectable** | **bool** |  | [optional] 
**banner** | **str** |  | [optional] 
**starttls** | **bool** |  | [optional] 
**response_time_ms** | **int** |  | [optional] 

## Example

```python
from mailodds.models.server_test_smtp_check import ServerTestSmtpCheck

# TODO update the JSON string below
json = "{}"
# create an instance of ServerTestSmtpCheck from a JSON string
server_test_smtp_check_instance = ServerTestSmtpCheck.from_json(json)
# print the JSON string representation of the object
print(ServerTestSmtpCheck.to_json())

# convert the object into a dict
server_test_smtp_check_dict = server_test_smtp_check_instance.to_dict()
# create an instance of ServerTestSmtpCheck from a dict
server_test_smtp_check_from_dict = ServerTestSmtpCheck.from_dict(server_test_smtp_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


