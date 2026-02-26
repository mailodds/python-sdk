# ListSendingDomains200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**List[SendingDomain]**](SendingDomain.md) |  | [optional] 

## Example

```python
from mailodds.models.list_sending_domains200_response import ListSendingDomains200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSendingDomains200Response from a JSON string
list_sending_domains200_response_instance = ListSendingDomains200Response.from_json(json)
# print the JSON string representation of the object
print(ListSendingDomains200Response.to_json())

# convert the object into a dict
list_sending_domains200_response_dict = list_sending_domains200_response_instance.to_dict()
# create an instance of ListSendingDomains200Response from a dict
list_sending_domains200_response_from_dict = ListSendingDomains200Response.from_dict(list_sending_domains200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


