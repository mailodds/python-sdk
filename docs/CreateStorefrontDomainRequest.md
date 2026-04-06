# CreateStorefrontDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | Fully qualified domain name | 
**store_id** | **str** | Store connection ID | 

## Example

```python
from mailodds.models.create_storefront_domain_request import CreateStorefrontDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStorefrontDomainRequest from a JSON string
create_storefront_domain_request_instance = CreateStorefrontDomainRequest.from_json(json)
# print the JSON string representation of the object
print(CreateStorefrontDomainRequest.to_json())

# convert the object into a dict
create_storefront_domain_request_dict = create_storefront_domain_request_instance.to_dict()
# create an instance of CreateStorefrontDomainRequest from a dict
create_storefront_domain_request_from_dict = CreateStorefrontDomainRequest.from_dict(create_storefront_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


