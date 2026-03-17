# AddContactRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**custom_fields** | **object** |  | [optional] 

## Example

```python
from mailodds.models.add_contact_request import AddContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddContactRequest from a JSON string
add_contact_request_instance = AddContactRequest.from_json(json)
# print the JSON string representation of the object
print(AddContactRequest.to_json())

# convert the object into a dict
add_contact_request_dict = add_contact_request_instance.to_dict()
# create an instance of AddContactRequest from a dict
add_contact_request_from_dict = AddContactRequest.from_dict(add_contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


