# StoreProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Product UUID | [optional] 
**store_id** | **str** | Store connection UUID | [optional] 
**external_id** | **str** | Product ID in the source store | [optional] 
**sku** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**price_current** | **float** | Current price | [optional] 
**price_original** | **float** | Original price (before discount) | [optional] 
**currency** | **str** |  | [optional] [default to 'USD']
**sale_start** | **datetime** |  | [optional] 
**sale_end** | **datetime** |  | [optional] 
**stock_status** | **str** |  | [optional] 
**stock_quantity** | **int** |  | [optional] 
**image_url** | **str** |  | [optional] 
**additional_images** | **List[str]** |  | [optional] 
**categories** | **List[str]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**product_url** | **str** |  | [optional] 
**variants** | **List[object]** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.store_product import StoreProduct

# TODO update the JSON string below
json = "{}"
# create an instance of StoreProduct from a JSON string
store_product_instance = StoreProduct.from_json(json)
# print the JSON string representation of the object
print(StoreProduct.to_json())

# convert the object into a dict
store_product_dict = store_product_instance.to_dict()
# create an instance of StoreProduct from a dict
store_product_from_dict = StoreProduct.from_dict(store_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


