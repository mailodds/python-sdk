# UpdateOooContactRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | Set to false to clear OOO status | [optional] 
**ooo_type** | **str** |  | [optional] [default to 'out_of_office']
**duration_days** | **int** |  | [optional] [default to 7]

## Example

```python
from mailodds.models.update_ooo_contact_request import UpdateOooContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOooContactRequest from a JSON string
update_ooo_contact_request_instance = UpdateOooContactRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOooContactRequest.to_json())

# convert the object into a dict
update_ooo_contact_request_dict = update_ooo_contact_request_instance.to_dict()
# create an instance of UpdateOooContactRequest from a dict
update_ooo_contact_request_from_dict = UpdateOooContactRequest.from_dict(update_ooo_contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


