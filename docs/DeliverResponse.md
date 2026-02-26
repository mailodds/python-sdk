# DeliverResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** | Unique request identifier | [optional] 
**message_id** | **str** | Unique message identifier | [optional] 
**status** | **str** | Delivery status | [optional] 
**delivery** | [**DeliverResponseDelivery**](DeliverResponseDelivery.md) |  | [optional] 
**validation** | **object** | Pre-send validation results (when validate_first is true) | [optional] 
**content_scan** | **object** | Content scan results | [optional] 

## Example

```python
from mailodds.models.deliver_response import DeliverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverResponse from a JSON string
deliver_response_instance = DeliverResponse.from_json(json)
# print the JSON string representation of the object
print(DeliverResponse.to_json())

# convert the object into a dict
deliver_response_dict = deliver_response_instance.to_dict()
# create an instance of DeliverResponse from a dict
deliver_response_from_dict = DeliverResponse.from_dict(deliver_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


