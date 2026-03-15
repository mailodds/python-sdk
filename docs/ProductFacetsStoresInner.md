# ProductFacetsStoresInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_id** | **str** |  | [optional] 
**store_name** | **str** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from mailodds.models.product_facets_stores_inner import ProductFacetsStoresInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductFacetsStoresInner from a JSON string
product_facets_stores_inner_instance = ProductFacetsStoresInner.from_json(json)
# print the JSON string representation of the object
print(ProductFacetsStoresInner.to_json())

# convert the object into a dict
product_facets_stores_inner_dict = product_facets_stores_inner_instance.to_dict()
# create an instance of ProductFacetsStoresInner from a dict
product_facets_stores_inner_from_dict = ProductFacetsStoresInner.from_dict(product_facets_stores_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


