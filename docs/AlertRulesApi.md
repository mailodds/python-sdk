# mailodds.AlertRulesApi

All URIs are relative to *https://api.mailodds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert_rule**](AlertRulesApi.md#create_alert_rule) | **POST** /v1/alert-rules | Create alert rule
[**delete_alert_rule**](AlertRulesApi.md#delete_alert_rule) | **DELETE** /v1/alert-rules/{rule_id} | Delete alert rule
[**get_alert_rule**](AlertRulesApi.md#get_alert_rule) | **GET** /v1/alert-rules/{rule_id} | Get alert rule
[**list_alert_rules**](AlertRulesApi.md#list_alert_rules) | **GET** /v1/alert-rules | List alert rules
[**update_alert_rule**](AlertRulesApi.md#update_alert_rule) | **PUT** /v1/alert-rules/{rule_id} | Update alert rule


# **create_alert_rule**
> CreateAlertRule201Response create_alert_rule(create_alert_rule_request)

Create alert rule

Create a new metric threshold alert rule. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_alert_rule201_response import CreateAlertRule201Response
from mailodds.models.create_alert_rule_request import CreateAlertRuleRequest
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
    api_instance = mailodds.AlertRulesApi(api_client)
    create_alert_rule_request = mailodds.CreateAlertRuleRequest() # CreateAlertRuleRequest | 

    try:
        # Create alert rule
        api_response = api_instance.create_alert_rule(create_alert_rule_request)
        print("The response of AlertRulesApi->create_alert_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertRulesApi->create_alert_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_alert_rule_request** | [**CreateAlertRuleRequest**](CreateAlertRuleRequest.md)|  | 

### Return type

[**CreateAlertRule201Response**](CreateAlertRule201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Alert rule created |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_rule**
> DeletePolicyRule200Response delete_alert_rule(rule_id)

Delete alert rule

Delete an alert rule. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.delete_policy_rule200_response import DeletePolicyRule200Response
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
    api_instance = mailodds.AlertRulesApi(api_client)
    rule_id = 'rule_id_example' # str | 

    try:
        # Delete alert rule
        api_response = api_instance.delete_alert_rule(rule_id)
        print("The response of AlertRulesApi->delete_alert_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertRulesApi->delete_alert_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

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
**200** | Alert rule deleted |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_rule**
> CreateAlertRule201Response get_alert_rule(rule_id)

Get alert rule

Get a single alert rule by ID. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_alert_rule201_response import CreateAlertRule201Response
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
    api_instance = mailodds.AlertRulesApi(api_client)
    rule_id = 'rule_id_example' # str | 

    try:
        # Get alert rule
        api_response = api_instance.get_alert_rule(rule_id)
        print("The response of AlertRulesApi->get_alert_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertRulesApi->get_alert_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

[**CreateAlertRule201Response**](CreateAlertRule201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alert rule details |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_rules**
> ListAlertRules200Response list_alert_rules()

List alert rules

List all configured alert rules. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.list_alert_rules200_response import ListAlertRules200Response
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
    api_instance = mailodds.AlertRulesApi(api_client)

    try:
        # List alert rules
        api_response = api_instance.list_alert_rules()
        print("The response of AlertRulesApi->list_alert_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertRulesApi->list_alert_rules: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAlertRules200Response**](ListAlertRules200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of alert rules |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_rule**
> CreateAlertRule201Response update_alert_rule(rule_id, update_alert_rule_request)

Update alert rule

Update an existing alert rule. Requires Growth+ plan.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_alert_rule201_response import CreateAlertRule201Response
from mailodds.models.update_alert_rule_request import UpdateAlertRuleRequest
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
    api_instance = mailodds.AlertRulesApi(api_client)
    rule_id = 'rule_id_example' # str | 
    update_alert_rule_request = mailodds.UpdateAlertRuleRequest() # UpdateAlertRuleRequest | 

    try:
        # Update alert rule
        api_response = api_instance.update_alert_rule(rule_id, update_alert_rule_request)
        print("The response of AlertRulesApi->update_alert_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertRulesApi->update_alert_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **update_alert_rule_request** | [**UpdateAlertRuleRequest**](UpdateAlertRuleRequest.md)|  | 

### Return type

[**CreateAlertRule201Response**](CreateAlertRule201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alert rule updated |  -  |
**403** | Forbidden - Insufficient permissions or no credits |  -  |
**404** | Resource not found |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

