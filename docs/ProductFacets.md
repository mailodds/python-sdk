# ProductFacets

Aggregated facets for the current query filters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[ProductFacetsCategoriesInner]**](ProductFacetsCategoriesInner.md) |  | [optional] 
**price_ranges** | [**List[ProductFacetsPriceRangesInner]**](ProductFacetsPriceRangesInner.md) |  | [optional] 
**stores** | [**List[ProductFacetsStoresInner]**](ProductFacetsStoresInner.md) |  | [optional] 

## Example

```python
from mailodds.models.product_facets import ProductFacets

# TODO update the JSON string below
json = "{}"
# create an instance of ProductFacets from a JSON string
product_facets_instance = ProductFacets.from_json(json)
# print the JSON string representation of the object
print(ProductFacets.to_json())

# convert the object into a dict
product_facets_dict = product_facets_instance.to_dict()
# create an instance of ProductFacets from a dict
product_facets_from_dict = ProductFacets.from_dict(product_facets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


