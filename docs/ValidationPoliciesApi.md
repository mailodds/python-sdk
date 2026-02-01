# mailodds.ValidationPoliciesApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_policy_rule**](ValidationPoliciesApi.md#add_policy_rule) | **POST** /v1/policies/{policy_id}/rules | Add rule to policy
[**create_policy**](ValidationPoliciesApi.md#create_policy) | **POST** /v1/policies | Create policy
[**create_policy_from_preset**](ValidationPoliciesApi.md#create_policy_from_preset) | **POST** /v1/policies/from-preset | Create policy from preset
[**delete_policy**](ValidationPoliciesApi.md#delete_policy) | **DELETE** /v1/policies/{policy_id} | Delete policy
[**delete_policy_rule**](ValidationPoliciesApi.md#delete_policy_rule) | **DELETE** /v1/policies/{policy_id}/rules/{rule_id} | Delete rule
[**get_policy**](ValidationPoliciesApi.md#get_policy) | **GET** /v1/policies/{policy_id} | Get policy
[**get_policy_presets**](ValidationPoliciesApi.md#get_policy_presets) | **GET** /v1/policies/presets | Get policy presets
[**list_policies**](ValidationPoliciesApi.md#list_policies) | **GET** /v1/policies | List policies
[**test_policy**](ValidationPoliciesApi.md#test_policy) | **POST** /v1/policies/test | Test policy evaluation
[**update_policy**](ValidationPoliciesApi.md#update_policy) | **PUT** /v1/policies/{policy_id} | Update policy


# **add_policy_rule**
> AddPolicyRule201Response add_policy_rule(policy_id, policy_rule)

Add rule to policy

Add a new rule to an existing policy.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.add_policy_rule201_response import AddPolicyRule201Response
from mailodds.models.policy_rule import PolicyRule
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.ValidationPoliciesApi(api_client)
    policy_id = 56 # int | 
    policy_rule = mailodds.PolicyRule() # PolicyRule | 

    try:
        # Add rule to policy
        api_response = api_instance.add_policy_rule(policy_id, policy_rule)
        print("The response of ValidationPoliciesApi->add_policy_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationPoliciesApi->add_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**|  | 
 **policy_rule** | [**PolicyRule**](PolicyRule.md)|  | 

### Return type

[**AddPolicyRule201Response**](AddPolicyRule201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Rule added |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**403** | Rule limit exceeded |  -  |
**404** | Policy not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy**
> PolicyResponse create_policy(create_policy_request)

Create policy

Create a new validation policy with rules.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_policy_request import CreatePolicyRequest
from mailodds.models.policy_response import PolicyResponse
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.ValidationPoliciesApi(api_client)
    create_policy_request = mailodds.CreatePolicyRequest() # CreatePolicyRequest | 

    try:
        # Create policy
        api_response = api_instance.create_policy(create_policy_request)
        print("The response of ValidationPoliciesApi->create_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationPoliciesApi->create_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_policy_request** | [**CreatePolicyRequest**](CreatePolicyRequest.md)|  | 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Policy created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**403** | Plan limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy_from_preset**
> PolicyResponse create_policy_from_preset(create_policy_from_preset_request)

Create policy from preset

Create a policy using a preset template.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_policy_from_preset_request import CreatePolicyFromPresetRequest
from mailodds.models.policy_response import PolicyResponse
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.ValidationPoliciesApi(api_client)
    create_policy_from_preset_request = mailodds.CreatePolicyFromPresetRequest() # CreatePolicyFromPresetRequest | 

    try:
        # Create policy from preset
        api_response = api_instance.create_policy_from_preset(create_policy_from_preset_request)
        print("The response of ValidationPoliciesApi->create_policy_from_preset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationPoliciesApi->create_policy_from_preset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_policy_from_preset_request** | [**CreatePolicyFromPresetRequest**](CreatePolicyFromPresetRequest.md)|  | 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Policy created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> DeletePolicy200Response delete_policy(policy_id)

Delete policy

Delete a policy and all its rules.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.delete_policy200_response import DeletePolicy200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.ValidationPoliciesApi(api_client)
    policy_id = 56 # int | 

    try:
        # Delete policy
        api_response = api_instance.delete_policy(policy_id)
        print("The response of ValidationPoliciesApi->delete_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationPoliciesApi->delete_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**|  | 

### Return type

[**DeletePolicy200Response**](DeletePolicy200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Policy deleted |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Policy not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_rule**
> DeletePolicyRule200Response delete_policy_rule(policy_id, rule_id)

Delete rule

Delete a rule from a policy.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.delete_policy_rule200_response import DeletePolicyRule200Response
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.ValidationPoliciesApi(api_client)
    policy_id = 56 # int | 
    rule_id = 56 # int | 

    try:
        # Delete rule
        api_response = api_instance.delete_policy_rule(policy_id, rule_id)
        print("The response of ValidationPoliciesApi->delete_policy_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationPoliciesApi->delete_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**|  | 
 **rule_id** | **int**|  | 

### Return type

[**DeletePolicyRule200Response**](DeletePolicyRule200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rule deleted |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Policy or rule not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> PolicyResponse get_policy(policy_id)

Get policy

Get a single policy with its rules.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.policy_response import PolicyResponse
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.ValidationPoliciesApi(api_client)
    policy_id = 56 # int | 

    try:
        # Get policy
        api_response = api_instance.get_policy(policy_id)
        print("The response of ValidationPoliciesApi->get_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationPoliciesApi->get_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**|  | 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Policy details |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Policy not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_presets**
> PolicyPresetsResponse get_policy_presets()

Get policy presets

Get available preset templates for quick policy creation.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.policy_presets_response import PolicyPresetsResponse
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.ValidationPoliciesApi(api_client)

    try:
        # Get policy presets
        api_response = api_instance.get_policy_presets()
        print("The response of ValidationPoliciesApi->get_policy_presets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationPoliciesApi->get_policy_presets: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PolicyPresetsResponse**](PolicyPresetsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available presets |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_policies**
> PolicyListResponse list_policies(include_rules=include_rules)

List policies

List all validation policies for your account. Includes plan limits.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.policy_list_response import PolicyListResponse
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.ValidationPoliciesApi(api_client)
    include_rules = False # bool | Include full rules in response (optional) (default to False)

    try:
        # List policies
        api_response = api_instance.list_policies(include_rules=include_rules)
        print("The response of ValidationPoliciesApi->list_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationPoliciesApi->list_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_rules** | **bool**| Include full rules in response | [optional] [default to False]

### Return type

[**PolicyListResponse**](PolicyListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of policies |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_policy**
> PolicyTestResponse test_policy(test_policy_request)

Test policy evaluation

Test how a policy would evaluate a validation result without affecting production.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.policy_test_response import PolicyTestResponse
from mailodds.models.test_policy_request import TestPolicyRequest
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.ValidationPoliciesApi(api_client)
    test_policy_request = mailodds.TestPolicyRequest() # TestPolicyRequest | 

    try:
        # Test policy evaluation
        api_response = api_instance.test_policy(test_policy_request)
        print("The response of ValidationPoliciesApi->test_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationPoliciesApi->test_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_policy_request** | [**TestPolicyRequest**](TestPolicyRequest.md)|  | 

### Return type

[**PolicyTestResponse**](PolicyTestResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test result |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Policy not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> PolicyResponse update_policy(policy_id, update_policy_request)

Update policy

Update a policy's settings (name, enabled, default).

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.policy_response import PolicyResponse
from mailodds.models.update_policy_request import UpdatePolicyRequest
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = mailodds.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailodds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailodds.ValidationPoliciesApi(api_client)
    policy_id = 56 # int | 
    update_policy_request = mailodds.UpdatePolicyRequest() # UpdatePolicyRequest | 

    try:
        # Update policy
        api_response = api_instance.update_policy(policy_id, update_policy_request)
        print("The response of ValidationPoliciesApi->update_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationPoliciesApi->update_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**|  | 
 **update_policy_request** | [**UpdatePolicyRequest**](UpdatePolicyRequest.md)|  | 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Policy updated |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Policy not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

