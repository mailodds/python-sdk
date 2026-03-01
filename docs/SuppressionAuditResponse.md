# SuppressionAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** | Unique request identifier | [optional] 
**entries** | [**List[SuppressionAuditResponseEntriesInner]**](SuppressionAuditResponseEntriesInner.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from mailodds.models.suppression_audit_response import SuppressionAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressionAuditResponse from a JSON string
suppression_audit_response_instance = SuppressionAuditResponse.from_json(json)
# print the JSON string representation of the object
print(SuppressionAuditResponse.to_json())

# convert the object into a dict
suppression_audit_response_dict = suppression_audit_response_instance.to_dict()
# create an instance of SuppressionAuditResponse from a dict
suppression_audit_response_from_dict = SuppressionAuditResponse.from_dict(suppression_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


