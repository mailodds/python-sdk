# ListWebhookDeliveries200ResponseDeliveriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**event_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**status_code** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**job_id** | **str** |  | [optional] 

## Example

```python
from mailodds.models.list_webhook_deliveries200_response_deliveries_inner import ListWebhookDeliveries200ResponseDeliveriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListWebhookDeliveries200ResponseDeliveriesInner from a JSON string
list_webhook_deliveries200_response_deliveries_inner_instance = ListWebhookDeliveries200ResponseDeliveriesInner.from_json(json)
# print the JSON string representation of the object
print(ListWebhookDeliveries200ResponseDeliveriesInner.to_json())

# convert the object into a dict
list_webhook_deliveries200_response_deliveries_inner_dict = list_webhook_deliveries200_response_deliveries_inner_instance.to_dict()
# create an instance of ListWebhookDeliveries200ResponseDeliveriesInner from a dict
list_webhook_deliveries200_response_deliveries_inner_from_dict = ListWebhookDeliveries200ResponseDeliveriesInner.from_dict(list_webhook_deliveries200_response_deliveries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


