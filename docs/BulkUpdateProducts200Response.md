# BulkUpdateProducts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**updated** | **int** |  | [optional] 

## Example

```python
from mailodds.models.bulk_update_products200_response import BulkUpdateProducts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateProducts200Response from a JSON string
bulk_update_products200_response_instance = BulkUpdateProducts200Response.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateProducts200Response.to_json())

# convert the object into a dict
bulk_update_products200_response_dict = bulk_update_products200_response_instance.to_dict()
# create an instance of BulkUpdateProducts200Response from a dict
bulk_update_products200_response_from_dict = BulkUpdateProducts200Response.from_dict(bulk_update_products200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


