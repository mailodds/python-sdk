# ValidationResponse

Flat validation response. Conditional fields are omitted (not null) when not applicable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | 
**email** | **str** |  | 
**status** | **str** | Validation status | 
**action** | **str** | Recommended action | 
**sub_status** | **str** | Detailed status reason. Omitted when none. | [optional] 
**domain** | **str** |  | 
**mx_found** | **bool** | Whether MX records were found for the domain | 
**mx_host** | **str** | Primary MX hostname. Omitted when MX not resolved. | [optional] 
**smtp_check** | **bool** | Whether SMTP verification passed. Omitted when SMTP not checked. | [optional] 
**catch_all** | **bool** | Whether domain is catch-all. Omitted when SMTP not checked. | [optional] 
**disposable** | **bool** | Whether domain is a known disposable email provider | 
**role_account** | **bool** | Whether address is a role account (e.g., info@, admin@) | 
**free_provider** | **bool** | Whether domain is a known free email provider (e.g., gmail.com) | 
**depth** | **str** | Validation depth used for this check | 
**processed_at** | **datetime** | ISO 8601 timestamp of validation | 
**suggested_email** | **str** | Typo correction suggestion. Omitted when no typo detected. | [optional] 
**retry_after_ms** | **int** | Suggested retry delay in milliseconds. Present only for retry_later action. | [optional] 
**suppression_match** | [**ValidationResponseSuppressionMatch**](ValidationResponseSuppressionMatch.md) |  | [optional] 
**policy_applied** | [**ValidationResponsePolicyApplied**](ValidationResponsePolicyApplied.md) |  | [optional] 

## Example

```python
from mailodds.models.validation_response import ValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationResponse from a JSON string
validation_response_instance = ValidationResponse.from_json(json)
# print the JSON string representation of the object
print(ValidationResponse.to_json())

# convert the object into a dict
validation_response_dict = validation_response_instance.to_dict()
# create an instance of ValidationResponse from a dict
validation_response_from_dict = ValidationResponse.from_dict(validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


