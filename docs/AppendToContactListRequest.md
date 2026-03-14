# AppendToContactListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_job_ids** | **List[str]** | Validation job IDs to append from | 
**include_catch_all** | **bool** | Include catch-all emails in addition to valid ones | [optional] [default to False]

## Example

```python
from mailodds.models.append_to_contact_list_request import AppendToContactListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppendToContactListRequest from a JSON string
append_to_contact_list_request_instance = AppendToContactListRequest.from_json(json)
# print the JSON string representation of the object
print(AppendToContactListRequest.to_json())

# convert the object into a dict
append_to_contact_list_request_dict = append_to_contact_list_request_instance.to_dict()
# create an instance of AppendToContactListRequest from a dict
append_to_contact_list_request_from_dict = AppendToContactListRequest.from_dict(append_to_contact_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


