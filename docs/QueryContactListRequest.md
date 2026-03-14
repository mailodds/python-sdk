# QueryContactListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[QueryContactListRequestFiltersInner]**](QueryContactListRequestFiltersInner.md) | Array of filter conditions | [optional] 
**page** | **int** |  | [optional] [default to 1]
**per_page** | **int** |  | [optional] [default to 100]

## Example

```python
from mailodds.models.query_contact_list_request import QueryContactListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryContactListRequest from a JSON string
query_contact_list_request_instance = QueryContactListRequest.from_json(json)
# print the JSON string representation of the object
print(QueryContactListRequest.to_json())

# convert the object into a dict
query_contact_list_request_dict = query_contact_list_request_instance.to_dict()
# create an instance of QueryContactListRequest from a dict
query_contact_list_request_from_dict = QueryContactListRequest.from_dict(query_contact_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


