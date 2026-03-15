# StoreConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Store connection UUID | [optional] 
**account_id** | **int** |  | [optional] 
**platform** | **str** | E-commerce platform | [optional] 
**store_name** | **str** |  | [optional] 
**store_url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**auth_method** | **str** |  | [optional] 
**product_count** | **int** | Number of active products | [optional] 
**last_synced_at** | **datetime** |  | [optional] 
**last_error** | **str** | Last sync error message | [optional] 
**sync_interval_seconds** | **int** | Auto-sync interval in seconds | [optional] [default to 3600]
**settings** | **object** | Platform-specific settings | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.store_connection import StoreConnection

# TODO update the JSON string below
json = "{}"
# create an instance of StoreConnection from a JSON string
store_connection_instance = StoreConnection.from_json(json)
# print the JSON string representation of the object
print(StoreConnection.to_json())

# convert the object into a dict
store_connection_dict = store_connection_instance.to_dict()
# create an instance of StoreConnection from a dict
store_connection_from_dict = StoreConnection.from_dict(store_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


