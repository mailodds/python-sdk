# BatchProductsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**created** | **int** | Products created | [optional] 
**updated** | **int** | Products updated | [optional] 
**errored** | **int** | Products that failed | [optional] 
**errors** | [**List[BatchProductsResponseErrorsInner]**](BatchProductsResponseErrorsInner.md) | Error details (max 20) | [optional] 

## Example

```python
from mailodds.models.batch_products_response import BatchProductsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchProductsResponse from a JSON string
batch_products_response_instance = BatchProductsResponse.from_json(json)
# print the JSON string representation of the object
print(BatchProductsResponse.to_json())

# convert the object into a dict
batch_products_response_dict = batch_products_response_instance.to_dict()
# create an instance of BatchProductsResponse from a dict
batch_products_response_from_dict = BatchProductsResponse.from_dict(batch_products_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


