# ContactList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Contact list UUID | [optional] 
**name** | **str** |  | [optional] 
**email_count** | **int** | Number of emails in the list | [optional] 
**tags** | **List[str]** |  | [optional] 
**source_job_ids** | **List[str]** | Validation job IDs this list was built from | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.contact_list import ContactList

# TODO update the JSON string below
json = "{}"
# create an instance of ContactList from a JSON string
contact_list_instance = ContactList.from_json(json)
# print the JSON string representation of the object
print(ContactList.to_json())

# convert the object into a dict
contact_list_dict = contact_list_instance.to_dict()
# create an instance of ContactList from a dict
contact_list_from_dict = ContactList.from_dict(contact_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


