# UpdatePixelSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pixel_subscribe_list_id** | **int** | Contact list ID for pixel subscriptions, or null to disable | 

## Example

```python
from mailodds.models.update_pixel_settings_request import UpdatePixelSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePixelSettingsRequest from a JSON string
update_pixel_settings_request_instance = UpdatePixelSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePixelSettingsRequest.to_json())

# convert the object into a dict
update_pixel_settings_request_dict = update_pixel_settings_request_instance.to_dict()
# create an instance of UpdatePixelSettingsRequest from a dict
update_pixel_settings_request_from_dict = UpdatePixelSettingsRequest.from_dict(update_pixel_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


