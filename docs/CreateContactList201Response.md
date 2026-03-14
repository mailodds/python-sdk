# CreateContactList201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**contact_list** | [**ContactList**](ContactList.md) |  | [optional] 

## Example

```python
from mailodds.models.create_contact_list201_response import CreateContactList201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactList201Response from a JSON string
create_contact_list201_response_instance = CreateContactList201Response.from_json(json)
# print the JSON string representation of the object
print(CreateContactList201Response.to_json())

# convert the object into a dict
create_contact_list201_response_dict = create_contact_list201_response_instance.to_dict()
# create an instance of CreateContactList201Response from a dict
create_contact_list201_response_from_dict = CreateContactList201Response.from_dict(create_contact_list201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


