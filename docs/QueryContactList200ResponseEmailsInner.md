# QueryContactList200ResponseEmailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**added_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.query_contact_list200_response_emails_inner import QueryContactList200ResponseEmailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of QueryContactList200ResponseEmailsInner from a JSON string
query_contact_list200_response_emails_inner_instance = QueryContactList200ResponseEmailsInner.from_json(json)
# print the JSON string representation of the object
print(QueryContactList200ResponseEmailsInner.to_json())

# convert the object into a dict
query_contact_list200_response_emails_inner_dict = query_contact_list200_response_emails_inner_instance.to_dict()
# create an instance of QueryContactList200ResponseEmailsInner from a dict
query_contact_list200_response_emails_inner_from_dict = QueryContactList200ResponseEmailsInner.from_dict(query_contact_list200_response_emails_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


