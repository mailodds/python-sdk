# WebhookEvent

Webhook payload delivered to your endpoint. Fields vary by event type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** | Event type | 
**timestamp** | **datetime** | When the event occurred | 
**job** | [**Job**](Job.md) |  | [optional] 
**message_id** | **str** | Message ID (present for message.* and delivery events) | [optional] 
**account_id** | **int** | Account ID (present for delivery events) | [optional] 
**domain_id** | **str** | Sending domain UUID (present for delivery events) | [optional] 
**to** | **str** | Recipient email (present for delivery events) | [optional] 
**status** | **str** | Delivery status (present for delivery events) | [optional] 
**smtp_code** | **int** | SMTP response code (present for bounced/deferred/failed) | [optional] 
**smtp_response** | **str** | SMTP diagnostic string (present for bounced/deferred/failed) | [optional] 
**mx_host** | **str** | MX host that handled delivery | [optional] 
**bounce_type** | **str** | Bounce classification (present for message.bounced) | [optional] 
**enhanced_status_code** | **str** | Enhanced SMTP status code (e.g., 5.1.1) | [optional] 
**attempts** | **int** | Number of delivery attempts | [optional] 
**isp** | **str** | Receiving ISP name | [optional] 
**is_mpp** | **bool** | Whether the open was from Apple Mail Privacy Protection | [optional] 
**ip_address** | **str** | Client IP (present for message.opened/clicked) | [optional] 
**user_agent** | **str** | Client user agent (present for message.opened/clicked) | [optional] 
**is_bot** | **bool** | Whether the event was triggered by a bot (present for message.opened/clicked) | [optional] 
**link_url** | **str** | Clicked URL (present for message.clicked) | [optional] 
**link_index** | **int** | Position of clicked link in message (present for message.clicked) | [optional] 

## Example

```python
from mailodds.models.webhook_event import WebhookEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEvent from a JSON string
webhook_event_instance = WebhookEvent.from_json(json)
# print the JSON string representation of the object
print(WebhookEvent.to_json())

# convert the object into a dict
webhook_event_dict = webhook_event_instance.to_dict()
# create an instance of WebhookEvent from a dict
webhook_event_from_dict = WebhookEvent.from_dict(webhook_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


