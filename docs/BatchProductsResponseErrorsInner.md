# BatchProductsResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from mailodds.models.batch_products_response_errors_inner import BatchProductsResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BatchProductsResponseErrorsInner from a JSON string
batch_products_response_errors_inner_instance = BatchProductsResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(BatchProductsResponseErrorsInner.to_json())

# convert the object into a dict
batch_products_response_errors_inner_dict = batch_products_response_errors_inner_instance.to_dict()
# create an instance of BatchProductsResponseErrorsInner from a dict
batch_products_response_errors_inner_from_dict = BatchProductsResponseErrorsInner.from_dict(batch_products_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


