# QueryContactListRequestFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to filter on | [optional] 
**operator** | **str** |  | [optional] 
**value** | **object** | Filter value | [optional] 

## Example

```python
from mailodds.models.query_contact_list_request_filters_inner import QueryContactListRequestFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of QueryContactListRequestFiltersInner from a JSON string
query_contact_list_request_filters_inner_instance = QueryContactListRequestFiltersInner.from_json(json)
# print the JSON string representation of the object
print(QueryContactListRequestFiltersInner.to_json())

# convert the object into a dict
query_contact_list_request_filters_inner_dict = query_contact_list_request_filters_inner_instance.to_dict()
# create an instance of QueryContactListRequestFiltersInner from a dict
query_contact_list_request_filters_inner_from_dict = QueryContactListRequestFiltersInner.from_dict(query_contact_list_request_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


