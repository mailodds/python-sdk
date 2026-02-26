# CreateListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | List name (unique per account) | 
**description** | **str** | Optional list description | [optional] 
**confirmation_redirect_url** | **str** | URL to redirect subscribers after confirmation | [optional] 
**confirmation_subject** | **str** | Custom confirmation email subject | [optional] 
**confirmation_from_name** | **str** | Custom sender name for confirmation emails | [optional] 

## Example

```python
from mailodds.models.create_list_request import CreateListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateListRequest from a JSON string
create_list_request_instance = CreateListRequest.from_json(json)
# print the JSON string representation of the object
print(CreateListRequest.to_json())

# convert the object into a dict
create_list_request_dict = create_list_request_instance.to_dict()
# create an instance of CreateListRequest from a dict
create_list_request_from_dict = CreateListRequest.from_dict(create_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


