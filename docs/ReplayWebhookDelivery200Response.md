# ReplayWebhookDelivery200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**delivery_id** | **int** |  | [optional] 

## Example

```python
from mailodds.models.replay_webhook_delivery200_response import ReplayWebhookDelivery200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReplayWebhookDelivery200Response from a JSON string
replay_webhook_delivery200_response_instance = ReplayWebhookDelivery200Response.from_json(json)
# print the JSON string representation of the object
print(ReplayWebhookDelivery200Response.to_json())

# convert the object into a dict
replay_webhook_delivery200_response_dict = replay_webhook_delivery200_response_instance.to_dict()
# create an instance of ReplayWebhookDelivery200Response from a dict
replay_webhook_delivery200_response_from_dict = ReplayWebhookDelivery200Response.from_dict(replay_webhook_delivery200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


