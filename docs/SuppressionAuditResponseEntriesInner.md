# SuppressionAuditResponseEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**event_type** | **str** | Audit event type | [optional] 
**event_category** | **str** |  | [optional] 
**details** | **object** | Event-specific details | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.suppression_audit_response_entries_inner import SuppressionAuditResponseEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressionAuditResponseEntriesInner from a JSON string
suppression_audit_response_entries_inner_instance = SuppressionAuditResponseEntriesInner.from_json(json)
# print the JSON string representation of the object
print(SuppressionAuditResponseEntriesInner.to_json())

# convert the object into a dict
suppression_audit_response_entries_inner_dict = suppression_audit_response_entries_inner_instance.to_dict()
# create an instance of SuppressionAuditResponseEntriesInner from a dict
suppression_audit_response_entries_inner_from_dict = SuppressionAuditResponseEntriesInner.from_dict(suppression_audit_response_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


