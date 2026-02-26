# UnsubscribeSubscriber200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriber** | [**Subscriber**](Subscriber.md) |  | [optional] 

## Example

```python
from mailodds.models.unsubscribe_subscriber200_response import UnsubscribeSubscriber200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UnsubscribeSubscriber200Response from a JSON string
unsubscribe_subscriber200_response_instance = UnsubscribeSubscriber200Response.from_json(json)
# print the JSON string representation of the object
print(UnsubscribeSubscriber200Response.to_json())

# convert the object into a dict
unsubscribe_subscriber200_response_dict = unsubscribe_subscriber200_response_instance.to_dict()
# create an instance of UnsubscribeSubscriber200Response from a dict
unsubscribe_subscriber200_response_from_dict = UnsubscribeSubscriber200Response.from_dict(unsubscribe_subscriber200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


