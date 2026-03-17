# GetDisengagedContacts200ResponsePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**has_next** | **bool** |  | [optional] 

## Example

```python
from mailodds.models.get_disengaged_contacts200_response_pagination import GetDisengagedContacts200ResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of GetDisengagedContacts200ResponsePagination from a JSON string
get_disengaged_contacts200_response_pagination_instance = GetDisengagedContacts200ResponsePagination.from_json(json)
# print the JSON string representation of the object
print(GetDisengagedContacts200ResponsePagination.to_json())

# convert the object into a dict
get_disengaged_contacts200_response_pagination_dict = get_disengaged_contacts200_response_pagination_instance.to_dict()
# create an instance of GetDisengagedContacts200ResponsePagination from a dict
get_disengaged_contacts200_response_pagination_from_dict = GetDisengagedContacts200ResponsePagination.from_dict(get_disengaged_contacts200_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


