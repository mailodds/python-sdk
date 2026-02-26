# DeliverRequestOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validate_first** | **bool** | Validate recipients before sending | [optional] 

## Example

```python
from mailodds.models.deliver_request_options import DeliverRequestOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverRequestOptions from a JSON string
deliver_request_options_instance = DeliverRequestOptions.from_json(json)
# print the JSON string representation of the object
print(DeliverRequestOptions.to_json())

# convert the object into a dict
deliver_request_options_dict = deliver_request_options_instance.to_dict()
# create an instance of DeliverRequestOptions from a dict
deliver_request_options_from_dict = DeliverRequestOptions.from_dict(deliver_request_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


