# SuppressDisengagedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inactive_days** | **int** | Days of inactivity threshold | [optional] [default to 180]
**min_sends** | **int** | Minimum sends to qualify | [optional] [default to 10]
**dry_run** | **bool** | Preview without suppressing | [optional] [default to True]

## Example

```python
from mailodds.models.suppress_disengaged_request import SuppressDisengagedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressDisengagedRequest from a JSON string
suppress_disengaged_request_instance = SuppressDisengagedRequest.from_json(json)
# print the JSON string representation of the object
print(SuppressDisengagedRequest.to_json())

# convert the object into a dict
suppress_disengaged_request_dict = suppress_disengaged_request_instance.to_dict()
# create an instance of SuppressDisengagedRequest from a dict
suppress_disengaged_request_from_dict = SuppressDisengagedRequest.from_dict(suppress_disengaged_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


