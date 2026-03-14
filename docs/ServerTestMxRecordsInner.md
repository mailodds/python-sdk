# ServerTestMxRecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**ip** | **str** |  | [optional] 

## Example

```python
from mailodds.models.server_test_mx_records_inner import ServerTestMxRecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ServerTestMxRecordsInner from a JSON string
server_test_mx_records_inner_instance = ServerTestMxRecordsInner.from_json(json)
# print the JSON string representation of the object
print(ServerTestMxRecordsInner.to_json())

# convert the object into a dict
server_test_mx_records_inner_dict = server_test_mx_records_inner_instance.to_dict()
# create an instance of ServerTestMxRecordsInner from a dict
server_test_mx_records_inner_from_dict = ServerTestMxRecordsInner.from_dict(server_test_mx_records_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


