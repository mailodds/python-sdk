# ValidateBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** | List of emails to validate | 
**depth** | **str** |  | [optional] [default to 'enhanced']
**policy_id** | **int** | Optional policy ID | [optional] 

## Example

```python
from mailodds.models.validate_batch_request import ValidateBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateBatchRequest from a JSON string
validate_batch_request_instance = ValidateBatchRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateBatchRequest.to_json())

# convert the object into a dict
validate_batch_request_dict = validate_batch_request_instance.to_dict()
# create an instance of ValidateBatchRequest from a dict
validate_batch_request_from_dict = ValidateBatchRequest.from_dict(validate_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


