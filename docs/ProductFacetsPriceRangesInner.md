# ProductFacetsPriceRangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | **str** | Price range label (e.g., &#39;0-10&#39;, &#39;500+&#39;) | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from mailodds.models.product_facets_price_ranges_inner import ProductFacetsPriceRangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductFacetsPriceRangesInner from a JSON string
product_facets_price_ranges_inner_instance = ProductFacetsPriceRangesInner.from_json(json)
# print the JSON string representation of the object
print(ProductFacetsPriceRangesInner.to_json())

# convert the object into a dict
product_facets_price_ranges_inner_dict = product_facets_price_ranges_inner_instance.to_dict()
# create an instance of ProductFacetsPriceRangesInner from a dict
product_facets_price_ranges_inner_from_dict = ProductFacetsPriceRangesInner.from_dict(product_facets_price_ranges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


