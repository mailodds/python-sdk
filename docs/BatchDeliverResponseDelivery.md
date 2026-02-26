# BatchDeliverResponseDelivery

Delivery routing info (present when status is queued)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool** | **str** | IP pool used | [optional] 
**lane** | **str** | Delivery lane (green or yellow) | [optional] 
**queued_at** | **datetime** | Timestamp when batch was queued | [optional] 

## Example

```python
from mailodds.models.batch_deliver_response_delivery import BatchDeliverResponseDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDeliverResponseDelivery from a JSON string
batch_deliver_response_delivery_instance = BatchDeliverResponseDelivery.from_json(json)
# print the JSON string representation of the object
print(BatchDeliverResponseDelivery.to_json())

# convert the object into a dict
batch_deliver_response_delivery_dict = batch_deliver_response_delivery_instance.to_dict()
# create an instance of BatchDeliverResponseDelivery from a dict
batch_deliver_response_delivery_from_dict = BatchDeliverResponseDelivery.from_dict(batch_deliver_response_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


