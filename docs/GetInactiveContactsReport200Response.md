# GetInactiveContactsReport200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**inactive_count** | **int** |  | [optional] 
**total_contacts** | **int** |  | [optional] 
**inactive_rate** | **float** |  | [optional] 
**by_list** | [**List[GetInactiveContactsReport200ResponseByListInner]**](GetInactiveContactsReport200ResponseByListInner.md) |  | [optional] 

## Example

```python
from mailodds.models.get_inactive_contacts_report200_response import GetInactiveContactsReport200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetInactiveContactsReport200Response from a JSON string
get_inactive_contacts_report200_response_instance = GetInactiveContactsReport200Response.from_json(json)
# print the JSON string representation of the object
print(GetInactiveContactsReport200Response.to_json())

# convert the object into a dict
get_inactive_contacts_report200_response_dict = get_inactive_contacts_report200_response_instance.to_dict()
# create an instance of GetInactiveContactsReport200Response from a dict
get_inactive_contacts_report200_response_from_dict = GetInactiveContactsReport200Response.from_dict(get_inactive_contacts_report200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


