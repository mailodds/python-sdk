# CreateSendingDomain201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | [**SendingDomain**](SendingDomain.md) |  | [optional] 

## Example

```python
from mailodds.models.create_sending_domain201_response import CreateSendingDomain201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSendingDomain201Response from a JSON string
create_sending_domain201_response_instance = CreateSendingDomain201Response.from_json(json)
# print the JSON string representation of the object
print(CreateSendingDomain201Response.to_json())

# convert the object into a dict
create_sending_domain201_response_dict = create_sending_domain201_response_instance.to_dict()
# create an instance of CreateSendingDomain201Response from a dict
create_sending_domain201_response_from_dict = CreateSendingDomain201Response.from_dict(create_sending_domain201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


