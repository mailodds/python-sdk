# ListServerTests200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**tests** | [**List[ServerTest]**](ServerTest.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from mailodds.models.list_server_tests200_response import ListServerTests200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListServerTests200Response from a JSON string
list_server_tests200_response_instance = ListServerTests200Response.from_json(json)
# print the JSON string representation of the object
print(ListServerTests200Response.to_json())

# convert the object into a dict
list_server_tests200_response_dict = list_server_tests200_response_instance.to_dict()
# create an instance of ListServerTests200Response from a dict
list_server_tests200_response_from_dict = ListServerTests200Response.from_dict(list_server_tests200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


