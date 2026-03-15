# QueryProducts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**products** | [**List[StoreProduct]**](StoreProduct.md) |  | [optional] 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**facets** | [**ProductFacets**](ProductFacets.md) |  | [optional] 

## Example

```python
from mailodds.models.query_products200_response import QueryProducts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QueryProducts200Response from a JSON string
query_products200_response_instance = QueryProducts200Response.from_json(json)
# print the JSON string representation of the object
print(QueryProducts200Response.to_json())

# convert the object into a dict
query_products200_response_dict = query_products200_response_instance.to_dict()
# create an instance of QueryProducts200Response from a dict
query_products200_response_from_dict = QueryProducts200Response.from_dict(query_products200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


