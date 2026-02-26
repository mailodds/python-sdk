# SubscriberList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | List UUID | [optional] 
**account_id** | **int** | Account ID | [optional] 
**name** | **str** | List name | [optional] 
**description** | **str** | List description | [optional] 
**confirmation_redirect_url** | **str** | Redirect URL after confirmation | [optional] 
**confirmation_subject** | **str** | Confirmation email subject | [optional] 
**confirmation_from_name** | **str** | Confirmation email sender name | [optional] 
**subscriber_count** | **int** | Total subscriber count | [optional] 
**confirmed_count** | **int** | Confirmed subscriber count | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.subscriber_list import SubscriberList

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriberList from a JSON string
subscriber_list_instance = SubscriberList.from_json(json)
# print the JSON string representation of the object
print(SubscriberList.to_json())

# convert the object into a dict
subscriber_list_dict = subscriber_list_instance.to_dict()
# create an instance of SubscriberList from a dict
subscriber_list_from_dict = SubscriberList.from_dict(subscriber_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


