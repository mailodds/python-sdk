# CreateWebhookCliSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forward_url** | **str** | Local URL where webhooks will be forwarded | [optional] 

## Example

```python
from mailodds.models.create_webhook_cli_session_request import CreateWebhookCliSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookCliSessionRequest from a JSON string
create_webhook_cli_session_request_instance = CreateWebhookCliSessionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookCliSessionRequest.to_json())

# convert the object into a dict
create_webhook_cli_session_request_dict = create_webhook_cli_session_request_instance.to_dict()
# create an instance of CreateWebhookCliSessionRequest from a dict
create_webhook_cli_session_request_from_dict = CreateWebhookCliSessionRequest.from_dict(create_webhook_cli_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


