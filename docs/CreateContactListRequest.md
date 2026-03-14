# CreateContactListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | List name | 
**source_job_id** | **str** | Single validation job ID to build list from | [optional] 
**source_job_ids** | **List[str]** | Multiple validation job IDs to merge into one list | [optional] 
**tags** | **List[str]** | Tags for categorization | [optional] 

## Example

```python
from mailodds.models.create_contact_list_request import CreateContactListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactListRequest from a JSON string
create_contact_list_request_instance = CreateContactListRequest.from_json(json)
# print the JSON string representation of the object
print(CreateContactListRequest.to_json())

# convert the object into a dict
create_contact_list_request_dict = create_contact_list_request_instance.to_dict()
# create an instance of CreateContactListRequest from a dict
create_contact_list_request_from_dict = CreateContactListRequest.from_dict(create_contact_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


