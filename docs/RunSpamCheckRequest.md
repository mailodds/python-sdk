# RunSpamCheckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_domain** | **str** | Sending domain to check | 
**links** | **List[str]** | URLs included in the email | [optional] 
**subject_preview** | **str** | Email subject line to analyze | [optional] 
**client_scores** | **object** | Client-side spam scores to include in analysis | [optional] 

## Example

```python
from mailodds.models.run_spam_check_request import RunSpamCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunSpamCheckRequest from a JSON string
run_spam_check_request_instance = RunSpamCheckRequest.from_json(json)
# print the JSON string representation of the object
print(RunSpamCheckRequest.to_json())

# convert the object into a dict
run_spam_check_request_dict = run_spam_check_request_instance.to_dict()
# create an instance of RunSpamCheckRequest from a dict
run_spam_check_request_from_dict = RunSpamCheckRequest.from_dict(run_spam_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


