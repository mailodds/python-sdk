# mailodds.BulkValidationApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_job**](BulkValidationApi.md#cancel_job) | **POST** /v1/jobs/{job_id}/cancel | Cancel a job
[**create_job**](BulkValidationApi.md#create_job) | **POST** /v1/jobs | Create bulk validation job (JSON)
[**create_job_from_s3**](BulkValidationApi.md#create_job_from_s3) | **POST** /v1/jobs/upload/s3 | Create job from S3 upload
[**create_job_upload**](BulkValidationApi.md#create_job_upload) | **POST** /v1/jobs/upload | Create bulk validation job (file upload)
[**delete_job**](BulkValidationApi.md#delete_job) | **DELETE** /v1/jobs/{job_id} | Delete a job
[**get_job**](BulkValidationApi.md#get_job) | **GET** /v1/jobs/{job_id} | Get job status
[**get_job_results**](BulkValidationApi.md#get_job_results) | **GET** /v1/jobs/{job_id}/results | Get job results
[**get_presigned_upload**](BulkValidationApi.md#get_presigned_upload) | **POST** /v1/jobs/upload/presigned | Get S3 presigned upload URL
[**list_jobs**](BulkValidationApi.md#list_jobs) | **GET** /v1/jobs | List validation jobs


# **cancel_job**
> JobResponse cancel_job(job_id)

Cancel a job

Cancel a pending or processing job. Partial results are preserved.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.job_response import JobResponse
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
    api_instance = mailodds.BulkValidationApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Cancel a job
        api_response = api_instance.cancel_job(job_id)
        print("The response of BulkValidationApi->cancel_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkValidationApi->cancel_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job cancelled |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job**
> JobResponse create_job(create_job_request)

Create bulk validation job (JSON)

Create a new bulk validation job by submitting a JSON array of emails.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_job_request import CreateJobRequest
from mailodds.models.job_response import JobResponse
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
    api_instance = mailodds.BulkValidationApi(api_client)
    create_job_request = mailodds.CreateJobRequest() # CreateJobRequest | 

    try:
        # Create bulk validation job (JSON)
        api_response = api_instance.create_job(create_job_request)
        print("The response of BulkValidationApi->create_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkValidationApi->create_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_job_request** | [**CreateJobRequest**](CreateJobRequest.md)|  | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Job created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job_from_s3**
> JobResponse create_job_from_s3(create_job_from_s3_request)

Create job from S3 upload

Create a validation job from a file previously uploaded to S3.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.create_job_from_s3_request import CreateJobFromS3Request
from mailodds.models.job_response import JobResponse
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
    api_instance = mailodds.BulkValidationApi(api_client)
    create_job_from_s3_request = mailodds.CreateJobFromS3Request() # CreateJobFromS3Request | 

    try:
        # Create job from S3 upload
        api_response = api_instance.create_job_from_s3(create_job_from_s3_request)
        print("The response of BulkValidationApi->create_job_from_s3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkValidationApi->create_job_from_s3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_job_from_s3_request** | [**CreateJobFromS3Request**](CreateJobFromS3Request.md)|  | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Job created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job_upload**
> JobResponse create_job_upload(file, dedup=dedup, metadata=metadata)

Create bulk validation job (file upload)

Create a new bulk validation job by uploading a CSV, Excel, or TXT file.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.job_response import JobResponse
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
    api_instance = mailodds.BulkValidationApi(api_client)
    file = None # bytearray | CSV, Excel (.xlsx, .xls), ODS, or TXT file
    dedup = False # bool | Remove duplicate emails (optional) (default to False)
    metadata = 'metadata_example' # str | JSON metadata for the job (optional)

    try:
        # Create bulk validation job (file upload)
        api_response = api_instance.create_job_upload(file, dedup=dedup, metadata=metadata)
        print("The response of BulkValidationApi->create_job_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkValidationApi->create_job_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| CSV, Excel (.xlsx, .xls), ODS, or TXT file | 
 **dedup** | **bool**| Remove duplicate emails | [optional] [default to False]
 **metadata** | **str**| JSON metadata for the job | [optional] 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Job created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job**
> DeleteJob200Response delete_job(job_id)

Delete a job

Permanently delete a completed or cancelled job and its results.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.delete_job200_response import DeleteJob200Response
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
    api_instance = mailodds.BulkValidationApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Delete a job
        api_response = api_instance.delete_job(job_id)
        print("The response of BulkValidationApi->delete_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkValidationApi->delete_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**DeleteJob200Response**](DeleteJob200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job deleted |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> JobResponse get_job(job_id)

Get job status

Get the status and details of a specific validation job.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.job_response import JobResponse
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
    api_instance = mailodds.BulkValidationApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Get job status
        api_response = api_instance.get_job(job_id)
        print("The response of BulkValidationApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkValidationApi->get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job details |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_results**
> ResultsResponse get_job_results(job_id, format=format, filter=filter, page=page, per_page=per_page)

Get job results

Download validation results in JSON, CSV, or NDJSON format.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.results_response import ResultsResponse
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
    api_instance = mailodds.BulkValidationApi(api_client)
    job_id = 'job_id_example' # str | 
    format = json # str |  (optional) (default to json)
    filter = 'filter_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = 1000 # int |  (optional) (default to 1000)

    try:
        # Get job results
        api_response = api_instance.get_job_results(job_id, format=format, filter=filter, page=page, per_page=per_page)
        print("The response of BulkValidationApi->get_job_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkValidationApi->get_job_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **format** | **str**|  | [optional] [default to json]
 **filter** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 1000]

### Return type

[**ResultsResponse**](ResultsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/x-ndjson

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Validation results |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_presigned_upload**
> PresignedUploadResponse get_presigned_upload(get_presigned_upload_request)

Get S3 presigned upload URL

Get a presigned URL for uploading large files (>10MB) directly to S3.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_presigned_upload_request import GetPresignedUploadRequest
from mailodds.models.presigned_upload_response import PresignedUploadResponse
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
    api_instance = mailodds.BulkValidationApi(api_client)
    get_presigned_upload_request = mailodds.GetPresignedUploadRequest() # GetPresignedUploadRequest | 

    try:
        # Get S3 presigned upload URL
        api_response = api_instance.get_presigned_upload(get_presigned_upload_request)
        print("The response of BulkValidationApi->get_presigned_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkValidationApi->get_presigned_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_presigned_upload_request** | [**GetPresignedUploadRequest**](GetPresignedUploadRequest.md)|  | 

### Return type

[**PresignedUploadResponse**](PresignedUploadResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Presigned upload credentials |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**503** | S3 not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs**
> JobListResponse list_jobs(page=page, per_page=per_page, status=status)

List validation jobs

List all validation jobs for the authenticated account.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.job_list_response import JobListResponse
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
    api_instance = mailodds.BulkValidationApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)
    status = 'status_example' # str |  (optional)

    try:
        # List validation jobs
        api_response = api_instance.list_jobs(page=page, per_page=per_page, status=status)
        print("The response of BulkValidationApi->list_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkValidationApi->list_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]
 **status** | **str**|  | [optional] 

### Return type

[**JobListResponse**](JobListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of jobs |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

