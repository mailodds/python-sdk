# GetReplyForwarding200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** |  | [optional] 
**forward_replies_to** | **str** |  | [optional] 

## Example

```python
from mailodds.models.get_reply_forwarding200_response import GetReplyForwarding200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetReplyForwarding200Response from a JSON string
get_reply_forwarding200_response_instance = GetReplyForwarding200Response.from_json(json)
# print the JSON string representation of the object
print(GetReplyForwarding200Response.to_json())

# convert the object into a dict
get_reply_forwarding200_response_dict = get_reply_forwarding200_response_instance.to_dict()
# create an instance of GetReplyForwarding200Response from a dict
get_reply_forwarding200_response_from_dict = GetReplyForwarding200Response.from_dict(get_reply_forwarding200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


