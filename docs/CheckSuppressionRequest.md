# CheckSuppressionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from mailodds.models.check_suppression_request import CheckSuppressionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckSuppressionRequest from a JSON string
check_suppression_request_instance = CheckSuppressionRequest.from_json(json)
# print the JSON string representation of the object
print(CheckSuppressionRequest.to_json())

# convert the object into a dict
check_suppression_request_dict = check_suppression_request_instance.to_dict()
# create an instance of CheckSuppressionRequest from a dict
check_suppression_request_from_dict = CheckSuppressionRequest.from_dict(check_suppression_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


