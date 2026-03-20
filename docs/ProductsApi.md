# mailodds.ProductsApi

All URIs are relative to *https://api.mailodds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_products**](ProductsApi.md#batch_products) | **POST** /v1/stores/{store_id}/products/batch | Batch push products
[**bulk_update_products**](ProductsApi.md#bulk_update_products) | **PATCH** /v1/store-products/bulk | Bulk update products
[**get_product**](ProductsApi.md#get_product) | **GET** /v1/store-products/{product_id} | Get a product
[**query_products**](ProductsApi.md#query_products) | **GET** /v1/store-products | Query products


# **batch_products**
> BatchProductsResponse batch_products(store_id, batch_products_request)

Batch push products

Push up to 100 products to a custom platform store. Creates new products or updates existing ones matched by external_id. Only available for stores with platform=custom.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.batch_products_request import BatchProductsRequest
from mailodds.models.batch_products_response import BatchProductsResponse
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
    api_instance = mailodds.ProductsApi(api_client)
    store_id = 'store_id_example' # str | 
    batch_products_request = mailodds.BatchProductsRequest() # BatchProductsRequest | 

    try:
        # Batch push products
        api_response = api_instance.batch_products(store_id, batch_products_request)
        print("The response of ProductsApi->batch_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->batch_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  | 
 **batch_products_request** | [**BatchProductsRequest**](BatchProductsRequest.md)|  | 

### Return type

[**BatchProductsResponse**](BatchProductsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch results |  -  |
**404** | Resource not found |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_products**
> BulkUpdateProducts200Response bulk_update_products(bulk_update_products_request)

Bulk update products

Bulk update product visibility. Maximum 500 products per request.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.bulk_update_products200_response import BulkUpdateProducts200Response
from mailodds.models.bulk_update_products_request import BulkUpdateProductsRequest
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
    api_instance = mailodds.ProductsApi(api_client)
    bulk_update_products_request = mailodds.BulkUpdateProductsRequest() # BulkUpdateProductsRequest | 

    try:
        # Bulk update products
        api_response = api_instance.bulk_update_products(bulk_update_products_request)
        print("The response of ProductsApi->bulk_update_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->bulk_update_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_update_products_request** | [**BulkUpdateProductsRequest**](BulkUpdateProductsRequest.md)|  | 

### Return type

[**BulkUpdateProducts200Response**](BulkUpdateProducts200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bulk update result |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> GetProduct200Response get_product(product_id)

Get a product

Get detailed information about a specific product.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.get_product200_response import GetProduct200Response
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
    api_instance = mailodds.ProductsApi(api_client)
    product_id = 'product_id_example' # str | 

    try:
        # Get a product
        api_response = api_instance.get_product(product_id)
        print("The response of ProductsApi->get_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 

### Return type

[**GetProduct200Response**](GetProduct200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product details |  -  |
**404** | Resource not found |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_products**
> QueryProducts200Response query_products(store_id=store_id, category=category, stock_status=stock_status, on_sale=on_sale, search=search, facets=facets, group_by_sku=group_by_sku, page=page, per_page=per_page)

Query products

Search and filter products across all connected stores. Supports faceted search and cross-store SKU deduplication for unified inventory views.

### Example

* Bearer Authentication (BearerAuth):

```python
import mailodds
from mailodds.models.query_products200_response import QueryProducts200Response
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
    api_instance = mailodds.ProductsApi(api_client)
    store_id = 'store_id_example' # str | Filter by store connection UUID (optional)
    category = 'category_example' # str | Filter by category name (optional)
    stock_status = 'stock_status_example' # str | Filter by stock status (optional)
    on_sale = True # bool | Filter to products currently on sale (optional)
    search = 'search_example' # str | Search by title or SKU (optional)
    facets = False # bool | Include facet aggregations (categories, price ranges, stores) (optional) (default to False)
    group_by_sku = False # bool | Merge products with same SKU across stores into unified entries (optional) (default to False)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)

    try:
        # Query products
        api_response = api_instance.query_products(store_id=store_id, category=category, stock_status=stock_status, on_sale=on_sale, search=search, facets=facets, group_by_sku=group_by_sku, page=page, per_page=per_page)
        print("The response of ProductsApi->query_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->query_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| Filter by store connection UUID | [optional] 
 **category** | **str**| Filter by category name | [optional] 
 **stock_status** | **str**| Filter by stock status | [optional] 
 **on_sale** | **bool**| Filter to products currently on sale | [optional] 
 **search** | **str**| Search by title or SKU | [optional] 
 **facets** | **bool**| Include facet aggregations (categories, price ranges, stores) | [optional] [default to False]
 **group_by_sku** | **bool**| Merge products with same SKU across stores into unified entries | [optional] [default to False]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]

### Return type

[**QueryProducts200Response**](QueryProducts200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product query results |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

