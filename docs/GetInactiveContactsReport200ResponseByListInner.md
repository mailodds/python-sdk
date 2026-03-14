# GetInactiveContactsReport200ResponseByListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** |  | [optional] 
**list_name** | **str** |  | [optional] 
**inactive_count** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mailodds.models.get_inactive_contacts_report200_response_by_list_inner import GetInactiveContactsReport200ResponseByListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInactiveContactsReport200ResponseByListInner from a JSON string
get_inactive_contacts_report200_response_by_list_inner_instance = GetInactiveContactsReport200ResponseByListInner.from_json(json)
# print the JSON string representation of the object
print(GetInactiveContactsReport200ResponseByListInner.to_json())

# convert the object into a dict
get_inactive_contacts_report200_response_by_list_inner_dict = get_inactive_contacts_report200_response_by_list_inner_instance.to_dict()
# create an instance of GetInactiveContactsReport200ResponseByListInner from a dict
get_inactive_contacts_report200_response_by_list_inner_from_dict = GetInactiveContactsReport200ResponseByListInner.from_dict(get_inactive_contacts_report200_response_by_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


