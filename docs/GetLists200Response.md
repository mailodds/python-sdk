# GetLists200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lists** | [**List[SubscriberList]**](SubscriberList.md) |  | [optional] 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 

## Example

```python
from mailodds.models.get_lists200_response import GetLists200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLists200Response from a JSON string
get_lists200_response_instance = GetLists200Response.from_json(json)
# print the JSON string representation of the object
print(GetLists200Response.to_json())

# convert the object into a dict
get_lists200_response_dict = get_lists200_response_instance.to_dict()
# create an instance of GetLists200Response from a dict
get_lists200_response_from_dict = GetLists200Response.from_dict(get_lists200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


