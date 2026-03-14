# AppendToContactList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**contact_list** | [**ContactList**](ContactList.md) |  | [optional] 
**added_count** | **int** | Number of new emails added | [optional] 
**candidate_count** | **int** | Total candidates from jobs | [optional] 
**duplicate_count** | **int** | Duplicates skipped | [optional] 
**breakdown** | **object** | Per-status breakdown of candidates | [optional] 

## Example

```python
from mailodds.models.append_to_contact_list200_response import AppendToContactList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AppendToContactList200Response from a JSON string
append_to_contact_list200_response_instance = AppendToContactList200Response.from_json(json)
# print the JSON string representation of the object
print(AppendToContactList200Response.to_json())

# convert the object into a dict
append_to_contact_list200_response_dict = append_to_contact_list200_response_instance.to_dict()
# create an instance of AppendToContactList200Response from a dict
append_to_contact_list200_response_from_dict = AppendToContactList200Response.from_dict(append_to_contact_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


