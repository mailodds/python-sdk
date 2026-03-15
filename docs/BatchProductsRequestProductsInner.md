# BatchProductsRequestProductsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** |  | 
**title** | **str** |  | 
**product_url** | **str** |  | 
**sku** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**price_current** | **float** |  | [optional] 
**price_original** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**stock_status** | **str** |  | [optional] 
**stock_quantity** | **int** |  | [optional] 
**image_url** | **str** |  | [optional] 
**additional_images** | **List[str]** |  | [optional] 
**categories** | **List[str]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**variants** | **List[object]** |  | [optional] 

## Example

```python
from mailodds.models.batch_products_request_products_inner import BatchProductsRequestProductsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BatchProductsRequestProductsInner from a JSON string
batch_products_request_products_inner_instance = BatchProductsRequestProductsInner.from_json(json)
# print the JSON string representation of the object
print(BatchProductsRequestProductsInner.to_json())

# convert the object into a dict
batch_products_request_products_inner_dict = batch_products_request_products_inner_instance.to_dict()
# create an instance of BatchProductsRequestProductsInner from a dict
batch_products_request_products_inner_from_dict = BatchProductsRequestProductsInner.from_dict(batch_products_request_products_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


