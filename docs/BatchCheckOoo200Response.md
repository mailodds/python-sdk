# BatchCheckOoo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[BatchCheckOoo200ResponseResultsInner]**](BatchCheckOoo200ResponseResultsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 
**ooo_count** | **int** |  | [optional] 

## Example

```python
from mailodds.models.batch_check_ooo200_response import BatchCheckOoo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BatchCheckOoo200Response from a JSON string
batch_check_ooo200_response_instance = BatchCheckOoo200Response.from_json(json)
# print the JSON string representation of the object
print(BatchCheckOoo200Response.to_json())

# convert the object into a dict
batch_check_ooo200_response_dict = batch_check_ooo200_response_instance.to_dict()
# create an instance of BatchCheckOoo200Response from a dict
batch_check_ooo200_response_from_dict = BatchCheckOoo200Response.from_dict(batch_check_ooo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


