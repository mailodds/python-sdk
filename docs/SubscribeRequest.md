# SubscribeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Subscriber email address | 
**name** | **str** | Subscriber name | [optional] 
**metadata** | **object** | Custom metadata key-value pairs | [optional] 
**page_url** | **str** | URL of the page where the subscription form was submitted (for consent proof) | [optional] 
**form_id** | **str** | Identifier of the form used to subscribe (for consent proof) | [optional] 

## Example

```python
from mailodds.models.subscribe_request import SubscribeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscribeRequest from a JSON string
subscribe_request_instance = SubscribeRequest.from_json(json)
# print the JSON string representation of the object
print(SubscribeRequest.to_json())

# convert the object into a dict
subscribe_request_dict = subscribe_request_instance.to_dict()
# create an instance of SubscribeRequest from a dict
subscribe_request_from_dict = SubscribeRequest.from_dict(subscribe_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


