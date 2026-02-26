# DeliverRequestStructuredData

JSON-LD structured data (object, array, or string). Max 10KB.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from mailodds.models.deliver_request_structured_data import DeliverRequestStructuredData

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverRequestStructuredData from a JSON string
deliver_request_structured_data_instance = DeliverRequestStructuredData.from_json(json)
# print the JSON string representation of the object
print(DeliverRequestStructuredData.to_json())

# convert the object into a dict
deliver_request_structured_data_dict = deliver_request_structured_data_instance.to_dict()
# create an instance of DeliverRequestStructuredData from a dict
deliver_request_structured_data_from_dict = DeliverRequestStructuredData.from_dict(deliver_request_structured_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


