# UpdateReplyForwardingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forward_replies_to** | **str** | Email to forward replies to, or null to disable | [optional] 

## Example

```python
from mailodds.models.update_reply_forwarding_request import UpdateReplyForwardingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateReplyForwardingRequest from a JSON string
update_reply_forwarding_request_instance = UpdateReplyForwardingRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateReplyForwardingRequest.to_json())

# convert the object into a dict
update_reply_forwarding_request_dict = update_reply_forwarding_request_instance.to_dict()
# create an instance of UpdateReplyForwardingRequest from a dict
update_reply_forwarding_request_from_dict = UpdateReplyForwardingRequest.from_dict(update_reply_forwarding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


