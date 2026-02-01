# RemoveSuppressionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | **List[str]** |  | 

## Example

```python
from mailodds.models.remove_suppression_request import RemoveSuppressionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveSuppressionRequest from a JSON string
remove_suppression_request_instance = RemoveSuppressionRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveSuppressionRequest.to_json())

# convert the object into a dict
remove_suppression_request_dict = remove_suppression_request_instance.to_dict()
# create an instance of RemoveSuppressionRequest from a dict
remove_suppression_request_from_dict = RemoveSuppressionRequest.from_dict(remove_suppression_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


