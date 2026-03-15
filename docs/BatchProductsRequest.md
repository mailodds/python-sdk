# BatchProductsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[BatchProductsRequestProductsInner]**](BatchProductsRequestProductsInner.md) |  | 

## Example

```python
from mailodds.models.batch_products_request import BatchProductsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchProductsRequest from a JSON string
batch_products_request_instance = BatchProductsRequest.from_json(json)
# print the JSON string representation of the object
print(BatchProductsRequest.to_json())

# convert the object into a dict
batch_products_request_dict = batch_products_request_instance.to_dict()
# create an instance of BatchProductsRequest from a dict
batch_products_request_from_dict = BatchProductsRequest.from_dict(batch_products_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


