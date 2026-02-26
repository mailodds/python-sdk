# BatchDeliverResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** | Unique request identifier | [optional] 
**total** | **int** | Total recipients submitted | [optional] 
**accepted** | **int** | Number of recipients accepted for delivery | [optional] 
**rejected** | [**List[BatchDeliverResponseRejectedInner]**](BatchDeliverResponseRejectedInner.md) | Recipients that were rejected (suppressed or failed validation) | [optional] 
**status** | **str** | Batch status | [optional] 
**delivery** | [**BatchDeliverResponseDelivery**](BatchDeliverResponseDelivery.md) |  | [optional] 

## Example

```python
from mailodds.models.batch_deliver_response import BatchDeliverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDeliverResponse from a JSON string
batch_deliver_response_instance = BatchDeliverResponse.from_json(json)
# print the JSON string representation of the object
print(BatchDeliverResponse.to_json())

# convert the object into a dict
batch_deliver_response_dict = batch_deliver_response_instance.to_dict()
# create an instance of BatchDeliverResponse from a dict
batch_deliver_response_from_dict = BatchDeliverResponse.from_dict(batch_deliver_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


