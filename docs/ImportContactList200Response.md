# ImportContactList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**imported** | **int** |  | [optional] 
**skipped** | **int** |  | [optional] 
**duplicates** | **int** |  | [optional] 
**errors** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**contact_list** | **object** |  | [optional] 

## Example

```python
from mailodds.models.import_contact_list200_response import ImportContactList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImportContactList200Response from a JSON string
import_contact_list200_response_instance = ImportContactList200Response.from_json(json)
# print the JSON string representation of the object
print(ImportContactList200Response.to_json())

# convert the object into a dict
import_contact_list200_response_dict = import_contact_list200_response_instance.to_dict()
# create an instance of ImportContactList200Response from a dict
import_contact_list200_response_from_dict = ImportContactList200Response.from_dict(import_contact_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


