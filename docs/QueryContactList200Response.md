# QueryContactList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**emails** | [**List[QueryContactList200ResponseEmailsInner]**](QueryContactList200ResponseEmailsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 

## Example

```python
from mailodds.models.query_contact_list200_response import QueryContactList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QueryContactList200Response from a JSON string
query_contact_list200_response_instance = QueryContactList200Response.from_json(json)
# print the JSON string representation of the object
print(QueryContactList200Response.to_json())

# convert the object into a dict
query_contact_list200_response_dict = query_contact_list200_response_instance.to_dict()
# create an instance of QueryContactList200Response from a dict
query_contact_list200_response_from_dict = QueryContactList200Response.from_dict(query_contact_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


