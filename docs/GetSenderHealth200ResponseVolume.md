# GetSenderHealth200ResponseVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent** | **int** |  | [optional] 
**delivered** | **int** |  | [optional] 
**bounced** | **int** |  | [optional] 
**complained** | **int** |  | [optional] 

## Example

```python
from mailodds.models.get_sender_health200_response_volume import GetSenderHealth200ResponseVolume

# TODO update the JSON string below
json = "{}"
# create an instance of GetSenderHealth200ResponseVolume from a JSON string
get_sender_health200_response_volume_instance = GetSenderHealth200ResponseVolume.from_json(json)
# print the JSON string representation of the object
print(GetSenderHealth200ResponseVolume.to_json())

# convert the object into a dict
get_sender_health200_response_volume_dict = get_sender_health200_response_volume_instance.to_dict()
# create an instance of GetSenderHealth200ResponseVolume from a dict
get_sender_health200_response_volume_from_dict = GetSenderHealth200ResponseVolume.from_dict(get_sender_health200_response_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


