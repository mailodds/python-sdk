# RunSpamCheck201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**spam_check** | [**SpamCheck**](SpamCheck.md) |  | [optional] 

## Example

```python
from mailodds.models.run_spam_check201_response import RunSpamCheck201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RunSpamCheck201Response from a JSON string
run_spam_check201_response_instance = RunSpamCheck201Response.from_json(json)
# print the JSON string representation of the object
print(RunSpamCheck201Response.to_json())

# convert the object into a dict
run_spam_check201_response_dict = run_spam_check201_response_instance.to_dict()
# create an instance of RunSpamCheck201Response from a dict
run_spam_check201_response_from_dict = RunSpamCheck201Response.from_dict(run_spam_check201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


