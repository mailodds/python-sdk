# BulkUpdateProductsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_ids** | **List[str]** | Product IDs to update | 
**is_active** | **bool** | Set product visibility | 

## Example

```python
from mailodds.models.bulk_update_products_request import BulkUpdateProductsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateProductsRequest from a JSON string
bulk_update_products_request_instance = BulkUpdateProductsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateProductsRequest.to_json())

# convert the object into a dict
bulk_update_products_request_dict = bulk_update_products_request_instance.to_dict()
# create an instance of BulkUpdateProductsRequest from a dict
bulk_update_products_request_from_dict = BulkUpdateProductsRequest.from_dict(bulk_update_products_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


