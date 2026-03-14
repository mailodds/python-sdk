# GetBounceRecords200ResponseRecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**bounce_type** | **str** |  | [optional] 
**smtp_code** | **int** |  | [optional] 
**enhanced_status** | **str** |  | [optional] 
**diagnostic** | **str** |  | [optional] 
**mx_host** | **str** |  | [optional] 
**bounced_at** | **datetime** |  | [optional] 

## Example

```python
from mailodds.models.get_bounce_records200_response_records_inner import GetBounceRecords200ResponseRecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetBounceRecords200ResponseRecordsInner from a JSON string
get_bounce_records200_response_records_inner_instance = GetBounceRecords200ResponseRecordsInner.from_json(json)
# print the JSON string representation of the object
print(GetBounceRecords200ResponseRecordsInner.to_json())

# convert the object into a dict
get_bounce_records200_response_records_inner_dict = get_bounce_records200_response_records_inner_instance.to_dict()
# create an instance of GetBounceRecords200ResponseRecordsInner from a dict
get_bounce_records200_response_records_inner_from_dict = GetBounceRecords200ResponseRecordsInner.from_dict(get_bounce_records200_response_records_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


