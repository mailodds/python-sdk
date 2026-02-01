# AddSuppressionRequestEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from mailodds.models.add_suppression_request_entries_inner import AddSuppressionRequestEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddSuppressionRequestEntriesInner from a JSON string
add_suppression_request_entries_inner_instance = AddSuppressionRequestEntriesInner.from_json(json)
# print the JSON string representation of the object
print(AddSuppressionRequestEntriesInner.to_json())

# convert the object into a dict
add_suppression_request_entries_inner_dict = add_suppression_request_entries_inner_instance.to_dict()
# create an instance of AddSuppressionRequestEntriesInner from a dict
add_suppression_request_entries_inner_from_dict = AddSuppressionRequestEntriesInner.from_dict(add_suppression_request_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


