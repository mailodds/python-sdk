# DeliverResponseDelivery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool** | **str** | IP pool used | [optional] 
**lane** | **str** | Delivery lane | [optional] 
**warmup_limited** | **bool** | Whether warmup throttling was applied | [optional] 

## Example

```python
from mailodds.models.deliver_response_delivery import DeliverResponseDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverResponseDelivery from a JSON string
deliver_response_delivery_instance = DeliverResponseDelivery.from_json(json)
# print the JSON string representation of the object
print(DeliverResponseDelivery.to_json())

# convert the object into a dict
deliver_response_delivery_dict = deliver_response_delivery_instance.to_dict()
# create an instance of DeliverResponseDelivery from a dict
deliver_response_delivery_from_dict = DeliverResponseDelivery.from_dict(deliver_response_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


