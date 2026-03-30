# mailodds.ReputationPoliciesApi

All URIs are relative to *https://api.mailodds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reputation_policy**](ReputationPoliciesApi.md#create_reputation_policy) | **POST** /v1/reputation-policies | Create a reputation policy
[**create_reputation_policy_from_preset**](ReputationPoliciesApi.md#create_reputation_policy_from_preset) | **POST** /v1/reputation-policies/from-preset | Create a reputation policy from preset
[**delete_reputation_policy**](ReputationPoliciesApi.md#delete_reputation_policy) | **DELETE** /v1/reputation-policies/{policy_id} | Delete a reputation policy
[**get_reputation_policy**](ReputationPoliciesApi.md#get_reputation_policy) | **GET** /v1/reputation-policies/{policy_id} | Get a reputation policy
[**get_reputation_policy_status**](ReputationPoliciesApi.md#get_reputation_policy_status) | **GET** /v1/reputation-policies/{policy_id}/status | Get reputation policy status
[**list_reputation_policies**](ReputationPoliciesApi.md#list_reputation_policies) | **GET** /v1/reputation-policies | List reputation policies
[**test_reputation_policy**](ReputationPoliciesApi.md#test_reputation_policy) | **POST** /v1/reputation-policies/{policy_id}/test | Test a reputation policy
[**update_reputation_policy**](ReputationPoliciesApi.md#update_reputation_policy) | **PUT** /v1/reputation-policies/{policy_id} | Update a reputation policy


# **create_reputation_policy**
> create_reputation_policy()

Create a reputation policy

Create a new reputation policy with custom rules and thresholds.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.ReputationPoliciesApi(api_client)

    try:
        # Create a reputation policy
        api_instance.create_reputation_policy()
    except Exception as e:
        print("Exception when calling ReputationPoliciesApi->create_reputation_policy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a reputation policy |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reputation_policy_from_preset**
> create_reputation_policy_from_preset()

Create a reputation policy from preset

Create a reputation policy from a predefined preset template.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.ReputationPoliciesApi(api_client)

    try:
        # Create a reputation policy from preset
        api_instance.create_reputation_policy_from_preset()
    except Exception as e:
        print("Exception when calling ReputationPoliciesApi->create_reputation_policy_from_preset: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a reputation policy from preset |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reputation_policy**
> delete_reputation_policy(policy_id)

Delete a reputation policy

Soft-delete a reputation policy.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.ReputationPoliciesApi(api_client)
    policy_id = 'policy_id_example' # str | 

    try:
        # Delete a reputation policy
        api_instance.delete_reputation_policy(policy_id)
    except Exception as e:
        print("Exception when calling ReputationPoliciesApi->delete_reputation_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a reputation policy |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reputation_policy**
> get_reputation_policy(policy_id)

Get a reputation policy

Retrieve a single reputation policy by ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.ReputationPoliciesApi(api_client)
    policy_id = 'policy_id_example' # str | 

    try:
        # Get a reputation policy
        api_instance.get_reputation_policy(policy_id)
    except Exception as e:
        print("Exception when calling ReputationPoliciesApi->get_reputation_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a reputation policy |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reputation_policy_status**
> get_reputation_policy_status(policy_id)

Get reputation policy status

Evaluate a policy and return per-domain status results.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.ReputationPoliciesApi(api_client)
    policy_id = 'policy_id_example' # str | 

    try:
        # Get reputation policy status
        api_instance.get_reputation_policy_status(policy_id)
    except Exception as e:
        print("Exception when calling ReputationPoliciesApi->get_reputation_policy_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get reputation policy status |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reputation_policies**
> list_reputation_policies()

List reputation policies

List all reputation policies for the account.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.ReputationPoliciesApi(api_client)

    try:
        # List reputation policies
        api_instance.list_reputation_policies()
    except Exception as e:
        print("Exception when calling ReputationPoliciesApi->list_reputation_policies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List reputation policies |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_reputation_policy**
> test_reputation_policy(policy_id)

Test a reputation policy

Dry-run evaluation of a reputation policy without applying actions.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.ReputationPoliciesApi(api_client)
    policy_id = 'policy_id_example' # str | 

    try:
        # Test a reputation policy
        api_instance.test_reputation_policy(policy_id)
    except Exception as e:
        print("Exception when calling ReputationPoliciesApi->test_reputation_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test a reputation policy |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reputation_policy**
> update_reputation_policy(policy_id)

Update a reputation policy

Update an existing reputation policy.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mailodds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailodds.Configuration(
    host = "https://api.mailodds.com"
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
    api_instance = mailodds.ReputationPoliciesApi(api_client)
    policy_id = 'policy_id_example' # str | 

    try:
        # Update a reputation policy
        api_instance.update_reputation_policy(policy_id)
    except Exception as e:
        print("Exception when calling ReputationPoliciesApi->update_reputation_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a reputation policy |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

