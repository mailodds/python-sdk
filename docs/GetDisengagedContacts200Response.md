# GetDisengagedContacts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 
**pagination** | [**GetDisengagedContacts200ResponsePagination**](GetDisengagedContacts200ResponsePagination.md) |  | [optional] 

## Example

```python
from mailodds.models.get_disengaged_contacts200_response import GetDisengagedContacts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDisengagedContacts200Response from a JSON string
get_disengaged_contacts200_response_instance = GetDisengagedContacts200Response.from_json(json)
# print the JSON string representation of the object
print(GetDisengagedContacts200Response.to_json())

# convert the object into a dict
get_disengaged_contacts200_response_dict = get_disengaged_contacts200_response_instance.to_dict()
# create an instance of GetDisengagedContacts200Response from a dict
get_disengaged_contacts200_response_from_dict = GetDisengagedContacts200Response.from_dict(get_disengaged_contacts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


