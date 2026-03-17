# CreateWebhookCliSession201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**sse_url** | **str** |  | [optional] 

## Example

```python
from mailodds.models.create_webhook_cli_session201_response import CreateWebhookCliSession201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookCliSession201Response from a JSON string
create_webhook_cli_session201_response_instance = CreateWebhookCliSession201Response.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookCliSession201Response.to_json())

# convert the object into a dict
create_webhook_cli_session201_response_dict = create_webhook_cli_session201_response_instance.to_dict()
# create an instance of CreateWebhookCliSession201Response from a dict
create_webhook_cli_session201_response_from_dict = CreateWebhookCliSession201Response.from_dict(create_webhook_cli_session201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


