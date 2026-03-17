# BatchCheckOooRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** | Email addresses to check | 

## Example

```python
from mailodds.models.batch_check_ooo_request import BatchCheckOooRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchCheckOooRequest from a JSON string
batch_check_ooo_request_instance = BatchCheckOooRequest.from_json(json)
# print the JSON string representation of the object
print(BatchCheckOooRequest.to_json())

# convert the object into a dict
batch_check_ooo_request_dict = batch_check_ooo_request_instance.to_dict()
# create an instance of BatchCheckOooRequest from a dict
batch_check_ooo_request_from_dict = BatchCheckOooRequest.from_dict(batch_check_ooo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


