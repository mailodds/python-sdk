# CorrectInboundMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correction** | **str** | Corrected classification label | 

## Example

```python
from mailodds.models.correct_inbound_message_request import CorrectInboundMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CorrectInboundMessageRequest from a JSON string
correct_inbound_message_request_instance = CorrectInboundMessageRequest.from_json(json)
# print the JSON string representation of the object
print(CorrectInboundMessageRequest.to_json())

# convert the object into a dict
correct_inbound_message_request_dict = correct_inbound_message_request_instance.to_dict()
# create an instance of CorrectInboundMessageRequest from a dict
correct_inbound_message_request_from_dict = CorrectInboundMessageRequest.from_dict(correct_inbound_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


