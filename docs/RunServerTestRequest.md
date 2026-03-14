# RunServerTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain to test | 

## Example

```python
from mailodds.models.run_server_test_request import RunServerTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunServerTestRequest from a JSON string
run_server_test_request_instance = RunServerTestRequest.from_json(json)
# print the JSON string representation of the object
print(RunServerTestRequest.to_json())

# convert the object into a dict
run_server_test_request_dict = run_server_test_request_instance.to_dict()
# create an instance of RunServerTestRequest from a dict
run_server_test_request_from_dict = RunServerTestRequest.from_dict(run_server_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


