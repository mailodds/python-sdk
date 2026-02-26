# CreateSendingDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name to add | 

## Example

```python
from mailodds.models.create_sending_domain_request import CreateSendingDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSendingDomainRequest from a JSON string
create_sending_domain_request_instance = CreateSendingDomainRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSendingDomainRequest.to_json())

# convert the object into a dict
create_sending_domain_request_dict = create_sending_domain_request_instance.to_dict()
# create an instance of CreateSendingDomainRequest from a dict
create_sending_domain_request_from_dict = CreateSendingDomainRequest.from_dict(create_sending_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


