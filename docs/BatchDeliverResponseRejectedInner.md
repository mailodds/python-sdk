# BatchDeliverResponseRejectedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**reason** | **str** | Rejection reason (suppressed, validation_rejected) | [optional] 
**status** | **str** | Validation status if rejected by validation | [optional] 
**sub_status** | **str** | Validation sub-status if rejected by validation | [optional] 

## Example

```python
from mailodds.models.batch_deliver_response_rejected_inner import BatchDeliverResponseRejectedInner

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDeliverResponseRejectedInner from a JSON string
batch_deliver_response_rejected_inner_instance = BatchDeliverResponseRejectedInner.from_json(json)
# print the JSON string representation of the object
print(BatchDeliverResponseRejectedInner.to_json())

# convert the object into a dict
batch_deliver_response_rejected_inner_dict = batch_deliver_response_rejected_inner_instance.to_dict()
# create an instance of BatchDeliverResponseRejectedInner from a dict
batch_deliver_response_rejected_inner_from_dict = BatchDeliverResponseRejectedInner.from_dict(batch_deliver_response_rejected_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


