# ValidateBatch200ResponseSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **int** |  | [optional] 
**invalid** | **int** |  | [optional] 
**catch_all** | **int** |  | [optional] 
**unknown** | **int** |  | [optional] 
**do_not_mail** | **int** |  | [optional] 

## Example

```python
from mailodds.models.validate_batch200_response_summary import ValidateBatch200ResponseSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateBatch200ResponseSummary from a JSON string
validate_batch200_response_summary_instance = ValidateBatch200ResponseSummary.from_json(json)
# print the JSON string representation of the object
print(ValidateBatch200ResponseSummary.to_json())

# convert the object into a dict
validate_batch200_response_summary_dict = validate_batch200_response_summary_instance.to_dict()
# create an instance of ValidateBatch200ResponseSummary from a dict
validate_batch200_response_summary_from_dict = ValidateBatch200ResponseSummary.from_dict(validate_batch200_response_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


