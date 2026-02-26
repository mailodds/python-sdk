# DeliverRequestToInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from mailodds.models.deliver_request_to_inner import DeliverRequestToInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverRequestToInner from a JSON string
deliver_request_to_inner_instance = DeliverRequestToInner.from_json(json)
# print the JSON string representation of the object
print(DeliverRequestToInner.to_json())

# convert the object into a dict
deliver_request_to_inner_dict = deliver_request_to_inner_instance.to_dict()
# create an instance of DeliverRequestToInner from a dict
deliver_request_to_inner_from_dict = DeliverRequestToInner.from_dict(deliver_request_to_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


