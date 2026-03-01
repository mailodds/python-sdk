# DeliverRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | [**List[DeliverRequestToInner]**](DeliverRequestToInner.md) | List of recipient email addresses | 
**var_from** | **str** | Sender email address (must match sending domain) | 
**subject** | **str** | Email subject line | 
**html** | **str** | HTML email body | [optional] 
**text** | **str** | Plain text email body | [optional] 
**domain_id** | **str** | Sending domain UUID | 
**reply_to** | **str** | Reply-to address | [optional] 
**headers** | **object** | Extra email headers | [optional] 
**tags** | **List[str]** | Tags for categorization | [optional] 
**campaign_type** | **str** | Campaign type for JSON-LD auto-generation | [optional] 
**structured_data** | [**DeliverRequestStructuredData**](DeliverRequestStructuredData.md) |  | [optional] 
**schema_data** | **Dict[str, str]** | Key-value pairs for campaign_type JSON-LD resolution (e.g., order_number, tracking_url) | [optional] 
**auto_detect_schema** | **bool** | Auto-detect JSON-LD structured data type from subject line | [optional] [default to False]
**ai_summary** | **str** | Hidden text summary for AI email assistants (max 500 characters) | [optional] 
**options** | [**DeliverRequestOptions**](DeliverRequestOptions.md) |  | [optional] 

## Example

```python
from mailodds.models.deliver_request import DeliverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverRequest from a JSON string
deliver_request_instance = DeliverRequest.from_json(json)
# print the JSON string representation of the object
print(DeliverRequest.to_json())

# convert the object into a dict
deliver_request_dict = deliver_request_instance.to_dict()
# create an instance of DeliverRequest from a dict
deliver_request_from_dict = DeliverRequest.from_dict(deliver_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


