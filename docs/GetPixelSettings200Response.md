# GetPixelSettings200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pixel_uuid** | **str** |  | [optional] 
**pixel_subscribe_list_id** | **int** |  | [optional] 

## Example

```python
from mailodds.models.get_pixel_settings200_response import GetPixelSettings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPixelSettings200Response from a JSON string
get_pixel_settings200_response_instance = GetPixelSettings200Response.from_json(json)
# print the JSON string representation of the object
print(GetPixelSettings200Response.to_json())

# convert the object into a dict
get_pixel_settings200_response_dict = get_pixel_settings200_response_instance.to_dict()
# create an instance of GetPixelSettings200Response from a dict
get_pixel_settings200_response_from_dict = GetPixelSettings200Response.from_dict(get_pixel_settings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


