# Subscriber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Subscriber UUID | [optional] 
**list_id** | **str** | List UUID | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**consent_source_ip** | **str** | IP address of subscription | [optional] 
**consent_page_url** | **str** | Page URL where form was submitted | [optional] 
**consent_form_id** | **str** | Form identifier | [optional] 
**consent_timestamp** | **datetime** |  | [optional] 
**confirmed_at** | **datetime** |  | [optional] 
**unsubscribed_at** | **datetime** |  | [optional] 
**validation_result** | **object** | Email validation result | [optional] 
**metadata** | **object** | Custom metadata | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.subscriber import Subscriber

# TODO update the JSON string below
json = "{}"
# create an instance of Subscriber from a JSON string
subscriber_instance = Subscriber.from_json(json)
# print the JSON string representation of the object
print(Subscriber.to_json())

# convert the object into a dict
subscriber_dict = subscriber_instance.to_dict()
# create an instance of Subscriber from a dict
subscriber_from_dict = Subscriber.from_dict(subscriber_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


