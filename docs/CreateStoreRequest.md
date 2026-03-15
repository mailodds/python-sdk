# CreateStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | **str** | E-commerce platform | 
**store_name** | **str** | Display name for the store | 
**store_url** | **str** | Store base URL | 
**auth_method** | **str** | Authentication method | 
**settings** | **object** | Platform-specific settings (e.g., API keys, feed URL) | [optional] 

## Example

```python
from mailodds.models.create_store_request import CreateStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStoreRequest from a JSON string
create_store_request_instance = CreateStoreRequest.from_json(json)
# print the JSON string representation of the object
print(CreateStoreRequest.to_json())

# convert the object into a dict
create_store_request_dict = create_store_request_instance.to_dict()
# create an instance of CreateStoreRequest from a dict
create_store_request_from_dict = CreateStoreRequest.from_dict(create_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


