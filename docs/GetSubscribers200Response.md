# GetSubscribers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscribers** | [**List[Subscriber]**](Subscriber.md) |  | [optional] 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 

## Example

```python
from mailodds.models.get_subscribers200_response import GetSubscribers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscribers200Response from a JSON string
get_subscribers200_response_instance = GetSubscribers200Response.from_json(json)
# print the JSON string representation of the object
print(GetSubscribers200Response.to_json())

# convert the object into a dict
get_subscribers200_response_dict = get_subscribers200_response_instance.to_dict()
# create an instance of GetSubscribers200Response from a dict
get_subscribers200_response_from_dict = GetSubscribers200Response.from_dict(get_subscribers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


