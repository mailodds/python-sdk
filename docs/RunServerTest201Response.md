# RunServerTest201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**test** | [**ServerTest**](ServerTest.md) |  | [optional] 

## Example

```python
from mailodds.models.run_server_test201_response import RunServerTest201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RunServerTest201Response from a JSON string
run_server_test201_response_instance = RunServerTest201Response.from_json(json)
# print the JSON string representation of the object
print(RunServerTest201Response.to_json())

# convert the object into a dict
run_server_test201_response_dict = run_server_test201_response_instance.to_dict()
# create an instance of RunServerTest201Response from a dict
run_server_test201_response_from_dict = RunServerTest201Response.from_dict(run_server_test201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


