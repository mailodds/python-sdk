# ListSpamChecks200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**spam_checks** | [**List[SpamCheck]**](SpamCheck.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from mailodds.models.list_spam_checks200_response import ListSpamChecks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSpamChecks200Response from a JSON string
list_spam_checks200_response_instance = ListSpamChecks200Response.from_json(json)
# print the JSON string representation of the object
print(ListSpamChecks200Response.to_json())

# convert the object into a dict
list_spam_checks200_response_dict = list_spam_checks200_response_instance.to_dict()
# create an instance of ListSpamChecks200Response from a dict
list_spam_checks200_response_from_dict = ListSpamChecks200Response.from_dict(list_spam_checks200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


