# DeleteWebhookCliSession200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from mailodds.models.delete_webhook_cli_session200_response import DeleteWebhookCliSession200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteWebhookCliSession200Response from a JSON string
delete_webhook_cli_session200_response_instance = DeleteWebhookCliSession200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteWebhookCliSession200Response.to_json())

# convert the object into a dict
delete_webhook_cli_session200_response_dict = delete_webhook_cli_session200_response_instance.to_dict()
# create an instance of DeleteWebhookCliSession200Response from a dict
delete_webhook_cli_session200_response_from_dict = DeleteWebhookCliSession200Response.from_dict(delete_webhook_cli_session200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


