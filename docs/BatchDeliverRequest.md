# BatchDeliverRequest

Same fields as DeliverRequest but 'to' accepts up to 100 recipients.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **List[str]** | List of recipient email addresses (max 100) | 
**var_from** | **str** |  | 
**subject** | **str** |  | 
**html** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**domain_id** | **str** | Sending domain UUID. Optional -- auto-resolved from the from address, or falls back to primary domain. | [optional] 
**reply_to** | **str** |  | [optional] 
**headers** | **object** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**campaign_type** | **str** |  | [optional] 
**structured_data** | [**BatchDeliverRequestStructuredData**](BatchDeliverRequestStructuredData.md) |  | [optional] 
**options** | **object** |  | [optional] 

## Example

```python
from mailodds.models.batch_deliver_request import BatchDeliverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDeliverRequest from a JSON string
batch_deliver_request_instance = BatchDeliverRequest.from_json(json)
# print the JSON string representation of the object
print(BatchDeliverRequest.to_json())

# convert the object into a dict
batch_deliver_request_dict = batch_deliver_request_instance.to_dict()
# create an instance of BatchDeliverRequest from a dict
batch_deliver_request_from_dict = BatchDeliverRequest.from_dict(batch_deliver_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


