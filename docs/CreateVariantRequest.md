# CreateVariantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Variant name (e.g., \&quot;Variant A\&quot;) | 
**subject** | **str** | Email subject line | 
**html** | **str** | HTML email body | [optional] 
**text** | **str** | Plain text email body | [optional] 
**weight** | **int** | Traffic weight percentage (all variant weights must sum to 100) | 

## Example

```python
from mailodds.models.create_variant_request import CreateVariantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVariantRequest from a JSON string
create_variant_request_instance = CreateVariantRequest.from_json(json)
# print the JSON string representation of the object
print(CreateVariantRequest.to_json())

# convert the object into a dict
create_variant_request_dict = create_variant_request_instance.to_dict()
# create an instance of CreateVariantRequest from a dict
create_variant_request_from_dict = CreateVariantRequest.from_dict(create_variant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


