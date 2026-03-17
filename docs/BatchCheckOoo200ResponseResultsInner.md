# BatchCheckOoo200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**is_ooo** | **bool** |  | [optional] 
**detected_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.batch_check_ooo200_response_results_inner import BatchCheckOoo200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BatchCheckOoo200ResponseResultsInner from a JSON string
batch_check_ooo200_response_results_inner_instance = BatchCheckOoo200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(BatchCheckOoo200ResponseResultsInner.to_json())

# convert the object into a dict
batch_check_ooo200_response_results_inner_dict = batch_check_ooo200_response_results_inner_instance.to_dict()
# create an instance of BatchCheckOoo200ResponseResultsInner from a dict
batch_check_ooo200_response_results_inner_from_dict = BatchCheckOoo200ResponseResultsInner.from_dict(batch_check_ooo200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


