# MailOdds Python SDK

The official Python client for email validation, transactional sending, and deliverability monitoring through the MailOdds API.

[![PyPI](https://img.shields.io/pypi/v/mailodds)](https://pypi.org/project/mailodds/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![API Docs](https://img.shields.io/badge/docs-api--reference-blue)](https://mailodds.com/api-reference)

## Installation

```bash
pip install mailodds
```

Requires Python 3.9+.

## Quick Start

```python
import os
import mailodds

configuration = mailodds.Configuration(
    host="https://api.mailodds.com/v1",
    access_token=os.environ["MAILODDS_API_KEY"],
)

with mailodds.ApiClient(configuration) as client:
    api = mailodds.EmailValidationApi(client)
    request = mailodds.ValidateRequest(email="user@example.com")
    result = api.validate_email(request)

    print(f"Status: {result.result.status}, Action: {result.result.action}")
```

## Error Handling

```python
from mailodds.rest import ApiException

try:
    result = api.validate_email(request)
except ApiException as e:
    print(f"API error {e.status}: {e.body}")
```

`ApiException` includes `status`, `body`, `headers`, and `reason` for debugging.

## MailOdds Platform

<details>
<summary>This SDK is part of the MailOdds email deliverability platform. Explore all capabilities.</summary>

- [Email Validation API](https://mailodds.com/email-validation-api) - Single and batch email verification with 25+ real-time checks
- [Bulk Email Validation](https://mailodds.com/bulk-email-validation) - Process lists of up to 500,000 emails per job
- [Email Sending API](https://mailodds.com/email-sending-api) - Transactional email delivery with DKIM dual signing
- [Email Deliverability Platform](https://mailodds.com/email-deliverability-platform) - Full-stack deliverability monitoring and optimization
- [DMARC Monitoring](https://mailodds.com/dmarc-monitoring) - Aggregate report analysis with policy recommendations
- [Sender Reputation](https://mailodds.com/sender-reputation) - Real-time sender health scoring and trend analysis
- [SMTP Server Test](https://mailodds.com/smtp-server-test) - DNS, MX, and SMTP connectivity diagnostics
- [API Reference](https://mailodds.com/api-reference) - Full endpoint documentation with request and response examples
- [Guide: Email Authentication](https://mailodds.com/guides/email-authentication) - SPF, DKIM, and DMARC setup guide
- [Security](https://mailodds.com/security) - Infrastructure security and data protection practices

</details>

## Features

- **Context manager support** - Use the ApiClient as a context manager for automatic resource cleanup
- **Typed models** - Every API request and response is a Python class with type hints for IDE autocompletion
- **Flexible auth** - Pass API keys via configuration or environment variables
- **Bulk validation** - Submit lists of up to 500,000 emails via JSON, file upload, or S3 presigned URL
- **Structured error handling** - ApiException carries HTTP status codes, response bodies, and headers for precise error recovery
- **Full platform coverage** - Access validation, sending, suppression lists, validation policies, and subscriber management from one package

## Why MailOdds

MailOdds is a complete email deliverability platform built for developers. Every email validated or sent through MailOdds passes through 25+ real-time checks including syntax verification, DNS and MX validation, SMTP mailbox probing, disposable domain detection, and role account identification.

The platform maintains sub-200ms median response times for single validations, 99.9% API uptime, and processes bulk lists of up to 500,000 emails per job. MailOdds supports 11 language SDKs, an MCP server for AI agent integration, a CLI for local development, and a WordPress plugin for no-code deployments.

All email sending uses DKIM dual signing with automated key rotation, and the deliverability monitoring stack covers DMARC aggregate reports, blacklist surveillance across 80+ DNSBLs, and real-time sender health scoring.

## API Reference

Full documentation is available at the [MailOdds API Reference](https://mailodds.com/api-reference).

All URIs are relative to `https://api.mailodds.com/v1`.

<details>
<summary>All Endpoints</summary>

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BulkValidationApi* | [**cancel_job**](docs/BulkValidationApi.md#cancel_job) | **POST** /v1/jobs/{job_id}/cancel | Cancel a job
*BulkValidationApi* | [**create_job**](docs/BulkValidationApi.md#create_job) | **POST** /v1/jobs | Create bulk validation job (JSON)
*BulkValidationApi* | [**create_job_from_s3**](docs/BulkValidationApi.md#create_job_from_s3) | **POST** /v1/jobs/upload/s3 | Create job from S3 upload
*BulkValidationApi* | [**create_job_upload**](docs/BulkValidationApi.md#create_job_upload) | **POST** /v1/jobs/upload | Create bulk validation job (file upload)
*BulkValidationApi* | [**delete_job**](docs/BulkValidationApi.md#delete_job) | **DELETE** /v1/jobs/{job_id} | Delete a job
*BulkValidationApi* | [**get_job**](docs/BulkValidationApi.md#get_job) | **GET** /v1/jobs/{job_id} | Get job status
*BulkValidationApi* | [**get_job_results**](docs/BulkValidationApi.md#get_job_results) | **GET** /v1/jobs/{job_id}/results | Get job results
*BulkValidationApi* | [**get_presigned_upload**](docs/BulkValidationApi.md#get_presigned_upload) | **POST** /v1/jobs/upload/presigned | Get S3 presigned upload URL
*BulkValidationApi* | [**list_jobs**](docs/BulkValidationApi.md#list_jobs) | **GET** /v1/jobs | List validation jobs
*EmailSendingApi* | [**deliver_batch**](docs/EmailSendingApi.md#deliver_batch) | **POST** /v1/deliver/batch | Send to multiple recipients (max 100)
*EmailSendingApi* | [**deliver_email**](docs/EmailSendingApi.md#deliver_email) | **POST** /v1/deliver | Send a single email
*EmailValidationApi* | [**validate_batch**](docs/EmailValidationApi.md#validate_batch) | **POST** /v1/validate/batch | Validate multiple emails (sync)
*EmailValidationApi* | [**validate_email**](docs/EmailValidationApi.md#validate_email) | **POST** /v1/validate | Validate single email
*SendingDomainsApi* | [**create_sending_domain**](docs/SendingDomainsApi.md#create_sending_domain) | **POST** /v1/sending-domains | Add a sending domain
*SendingDomainsApi* | [**delete_sending_domain**](docs/SendingDomainsApi.md#delete_sending_domain) | **DELETE** /v1/sending-domains/{domain_id} | Delete a sending domain
*SendingDomainsApi* | [**get_sending_domain**](docs/SendingDomainsApi.md#get_sending_domain) | **GET** /v1/sending-domains/{domain_id} | Get a sending domain
*SendingDomainsApi* | [**get_sending_domain_identity_score**](docs/SendingDomainsApi.md#get_sending_domain_identity_score) | **GET** /v1/sending-domains/{domain_id}/identity-score | Get domain identity score
*SendingDomainsApi* | [**get_sending_stats**](docs/SendingDomainsApi.md#get_sending_stats) | **GET** /v1/sending-stats | Get sending statistics
*SendingDomainsApi* | [**list_sending_domains**](docs/SendingDomainsApi.md#list_sending_domains) | **GET** /v1/sending-domains | List sending domains
*SendingDomainsApi* | [**verify_sending_domain**](docs/SendingDomainsApi.md#verify_sending_domain) | **POST** /v1/sending-domains/{domain_id}/verify | Verify domain DNS records
*SubscriberListsApi* | [**confirm_subscription**](docs/SubscriberListsApi.md#confirm_subscription) | **GET** /v1/confirm/{token} | Confirm subscription
*SubscriberListsApi* | [**create_list**](docs/SubscriberListsApi.md#create_list) | **POST** /v1/lists | Create a subscriber list
*SubscriberListsApi* | [**delete_list**](docs/SubscriberListsApi.md#delete_list) | **DELETE** /v1/lists/{list_id} | Delete a subscriber list
*SubscriberListsApi* | [**get_list**](docs/SubscriberListsApi.md#get_list) | **GET** /v1/lists/{list_id} | Get a subscriber list
*SubscriberListsApi* | [**get_lists**](docs/SubscriberListsApi.md#get_lists) | **GET** /v1/lists | List subscriber lists
*SubscriberListsApi* | [**get_subscribers**](docs/SubscriberListsApi.md#get_subscribers) | **GET** /v1/lists/{list_id}/subscribers | List subscribers
*SubscriberListsApi* | [**subscribe**](docs/SubscriberListsApi.md#subscribe) | **POST** /v1/subscribe/{list_id} | Subscribe to a list
*SubscriberListsApi* | [**unsubscribe_subscriber**](docs/SubscriberListsApi.md#unsubscribe_subscriber) | **DELETE** /v1/lists/{list_id}/subscribers/{subscriber_id} | Unsubscribe a subscriber
*SuppressionListsApi* | [**add_suppression**](docs/SuppressionListsApi.md#add_suppression) | **POST** /v1/suppression | Add suppression entries
*SuppressionListsApi* | [**check_suppression**](docs/SuppressionListsApi.md#check_suppression) | **POST** /v1/suppression/check | Check suppression status
*SuppressionListsApi* | [**get_suppression_audit_log**](docs/SuppressionListsApi.md#get_suppression_audit_log) | **GET** /v1/suppression/audit | Get suppression audit log
*SuppressionListsApi* | [**get_suppression_stats**](docs/SuppressionListsApi.md#get_suppression_stats) | **GET** /v1/suppression/stats | Get suppression statistics
*SuppressionListsApi* | [**list_suppression**](docs/SuppressionListsApi.md#list_suppression) | **GET** /v1/suppression | List suppression entries
*SuppressionListsApi* | [**remove_suppression**](docs/SuppressionListsApi.md#remove_suppression) | **DELETE** /v1/suppression | Remove suppression entries
*SystemApi* | [**get_telemetry_summary**](docs/SystemApi.md#get_telemetry_summary) | **GET** /v1/telemetry/summary | Get validation telemetry
*SystemApi* | [**health_check**](docs/SystemApi.md#health_check) | **GET** /health | Health check
*ValidationPoliciesApi* | [**add_policy_rule**](docs/ValidationPoliciesApi.md#add_policy_rule) | **POST** /v1/policies/{policy_id}/rules | Add rule to policy
*ValidationPoliciesApi* | [**create_policy**](docs/ValidationPoliciesApi.md#create_policy) | **POST** /v1/policies | Create policy
*ValidationPoliciesApi* | [**create_policy_from_preset**](docs/ValidationPoliciesApi.md#create_policy_from_preset) | **POST** /v1/policies/from-preset | Create policy from preset
*ValidationPoliciesApi* | [**delete_policy**](docs/ValidationPoliciesApi.md#delete_policy) | **DELETE** /v1/policies/{policy_id} | Delete policy
*ValidationPoliciesApi* | [**delete_policy_rule**](docs/ValidationPoliciesApi.md#delete_policy_rule) | **DELETE** /v1/policies/{policy_id}/rules/{rule_id} | Delete rule
*ValidationPoliciesApi* | [**get_policy**](docs/ValidationPoliciesApi.md#get_policy) | **GET** /v1/policies/{policy_id} | Get policy
*ValidationPoliciesApi* | [**get_policy_presets**](docs/ValidationPoliciesApi.md#get_policy_presets) | **GET** /v1/policies/presets | Get policy presets
*ValidationPoliciesApi* | [**list_policies**](docs/ValidationPoliciesApi.md#list_policies) | **GET** /v1/policies | List policies
*ValidationPoliciesApi* | [**test_policy**](docs/ValidationPoliciesApi.md#test_policy) | **POST** /v1/policies/test | Test policy evaluation
*ValidationPoliciesApi* | [**update_policy**](docs/ValidationPoliciesApi.md#update_policy) | **PUT** /v1/policies/{policy_id} | Update policy

</details>

<details>
<summary>All Models</summary>

 - [AddPolicyRule201Response](docs/AddPolicyRule201Response.md)
 - [AddSuppressionRequest](docs/AddSuppressionRequest.md)
 - [AddSuppressionRequestEntriesInner](docs/AddSuppressionRequestEntriesInner.md)
 - [AddSuppressionResponse](docs/AddSuppressionResponse.md)
 - [BatchDeliverRequest](docs/BatchDeliverRequest.md)
 - [BatchDeliverRequestStructuredData](docs/BatchDeliverRequestStructuredData.md)
 - [BatchDeliverResponse](docs/BatchDeliverResponse.md)
 - [BatchDeliverResponseDelivery](docs/BatchDeliverResponseDelivery.md)
 - [BatchDeliverResponseRejectedInner](docs/BatchDeliverResponseRejectedInner.md)
 - [CheckSuppressionRequest](docs/CheckSuppressionRequest.md)
 - [ConfirmSubscription200Response](docs/ConfirmSubscription200Response.md)
 - [CreateJobFromS3Request](docs/CreateJobFromS3Request.md)
 - [CreateJobRequest](docs/CreateJobRequest.md)
 - [CreateList201Response](docs/CreateList201Response.md)
 - [CreateListRequest](docs/CreateListRequest.md)
 - [CreatePolicyFromPresetRequest](docs/CreatePolicyFromPresetRequest.md)
 - [CreatePolicyRequest](docs/CreatePolicyRequest.md)
 - [CreateSendingDomain201Response](docs/CreateSendingDomain201Response.md)
 - [CreateSendingDomainRequest](docs/CreateSendingDomainRequest.md)
 - [DeleteJob200Response](docs/DeleteJob200Response.md)
 - [DeletePolicy200Response](docs/DeletePolicy200Response.md)
 - [DeletePolicyRule200Response](docs/DeletePolicyRule200Response.md)
 - [DeliverRequest](docs/DeliverRequest.md)
 - [DeliverRequestOptions](docs/DeliverRequestOptions.md)
 - [DeliverRequestStructuredData](docs/DeliverRequestStructuredData.md)
 - [DeliverRequestToInner](docs/DeliverRequestToInner.md)
 - [DeliverResponse](docs/DeliverResponse.md)
 - [DeliverResponseDelivery](docs/DeliverResponseDelivery.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [GetLists200Response](docs/GetLists200Response.md)
 - [GetPresignedUploadRequest](docs/GetPresignedUploadRequest.md)
 - [GetSendingDomainIdentityScore200Response](docs/GetSendingDomainIdentityScore200Response.md)
 - [GetSendingStats200Response](docs/GetSendingStats200Response.md)
 - [GetSendingStats200ResponseStats](docs/GetSendingStats200ResponseStats.md)
 - [GetSubscribers200Response](docs/GetSubscribers200Response.md)
 - [HealthCheck200Response](docs/HealthCheck200Response.md)
 - [IdentityScoreCheck](docs/IdentityScoreCheck.md)
 - [Job](docs/Job.md)
 - [JobArtifacts](docs/JobArtifacts.md)
 - [JobListResponse](docs/JobListResponse.md)
 - [JobResponse](docs/JobResponse.md)
 - [JobSummary](docs/JobSummary.md)
 - [ListSendingDomains200Response](docs/ListSendingDomains200Response.md)
 - [Pagination](docs/Pagination.md)
 - [Policy](docs/Policy.md)
 - [PolicyListResponse](docs/PolicyListResponse.md)
 - [PolicyListResponseLimits](docs/PolicyListResponseLimits.md)
 - [PolicyPresetsResponse](docs/PolicyPresetsResponse.md)
 - [PolicyPresetsResponsePresetsInner](docs/PolicyPresetsResponsePresetsInner.md)
 - [PolicyResponse](docs/PolicyResponse.md)
 - [PolicyRule](docs/PolicyRule.md)
 - [PolicyRuleAction](docs/PolicyRuleAction.md)
 - [PolicyTestResponse](docs/PolicyTestResponse.md)
 - [PresignedUploadResponse](docs/PresignedUploadResponse.md)
 - [PresignedUploadResponseUpload](docs/PresignedUploadResponseUpload.md)
 - [RemoveSuppression200Response](docs/RemoveSuppression200Response.md)
 - [RemoveSuppressionRequest](docs/RemoveSuppressionRequest.md)
 - [ResultsResponse](docs/ResultsResponse.md)
 - [SendingDomain](docs/SendingDomain.md)
 - [SendingDomainDnsRecords](docs/SendingDomainDnsRecords.md)
 - [SendingDomainDnsRecordsNs](docs/SendingDomainDnsRecordsNs.md)
 - [SendingDomainIdentityScore](docs/SendingDomainIdentityScore.md)
 - [SendingDomainIdentityScoreBreakdown](docs/SendingDomainIdentityScoreBreakdown.md)
 - [SubscribeRequest](docs/SubscribeRequest.md)
 - [Subscriber](docs/Subscriber.md)
 - [SubscriberList](docs/SubscriberList.md)
 - [SuppressionAuditResponse](docs/SuppressionAuditResponse.md)
 - [SuppressionAuditResponseEntriesInner](docs/SuppressionAuditResponseEntriesInner.md)
 - [SuppressionCheckResponse](docs/SuppressionCheckResponse.md)
 - [SuppressionEntry](docs/SuppressionEntry.md)
 - [SuppressionListResponse](docs/SuppressionListResponse.md)
 - [SuppressionStatsResponse](docs/SuppressionStatsResponse.md)
 - [SuppressionStatsResponseByType](docs/SuppressionStatsResponseByType.md)
 - [TelemetrySummary](docs/TelemetrySummary.md)
 - [TelemetrySummaryRates](docs/TelemetrySummaryRates.md)
 - [TelemetrySummaryTopDomainsInner](docs/TelemetrySummaryTopDomainsInner.md)
 - [TelemetrySummaryTopReasonsInner](docs/TelemetrySummaryTopReasonsInner.md)
 - [TelemetrySummaryTotals](docs/TelemetrySummaryTotals.md)
 - [TestPolicyRequest](docs/TestPolicyRequest.md)
 - [TestPolicyRequestTestResult](docs/TestPolicyRequestTestResult.md)
 - [UnsubscribeSubscriber200Response](docs/UnsubscribeSubscriber200Response.md)
 - [UpdatePolicyRequest](docs/UpdatePolicyRequest.md)
 - [ValidateBatch200Response](docs/ValidateBatch200Response.md)
 - [ValidateBatch200ResponseSummary](docs/ValidateBatch200ResponseSummary.md)
 - [ValidateBatchRequest](docs/ValidateBatchRequest.md)
 - [ValidateRequest](docs/ValidateRequest.md)
 - [ValidationResponse](docs/ValidationResponse.md)
 - [ValidationResponsePolicyApplied](docs/ValidationResponsePolicyApplied.md)
 - [ValidationResponseSuppressionMatch](docs/ValidationResponseSuppressionMatch.md)
 - [ValidationResult](docs/ValidationResult.md)
 - [ValidationResultSuppression](docs/ValidationResultSuppression.md)
 - [WebhookEvent](docs/WebhookEvent.md)

</details>

## Other SDKs

| Language | Package | Source |
|----------|---------|--------|
| [Python](https://mailodds.com/sdks) | [PyPI](https://pypi.org/project/mailodds/) | [GitHub](https://github.com/mailodds/python-sdk) |
| [TypeScript](https://mailodds.com/sdks) | [npm](https://www.npmjs.com/package/@mailodds/sdk) | [GitHub](https://github.com/mailodds/typescript-sdk) |
| [PHP](https://mailodds.com/sdks) | [Packagist](https://packagist.org/packages/mailodds/mailodds-php) | [GitHub](https://github.com/mailodds/php-sdk) |
| [Java](https://mailodds.com/sdks) | [GitHub](https://github.com/mailodds/java-sdk) | [GitHub](https://github.com/mailodds/java-sdk) |
| [Go](https://mailodds.com/sdks) | [pkg.go.dev](https://pkg.go.dev/github.com/mailodds/go-sdk) | [GitHub](https://github.com/mailodds/go-sdk) |
| [C# / .NET](https://mailodds.com/sdks) | [GitHub](https://github.com/mailodds/csharp-sdk) | [GitHub](https://github.com/mailodds/csharp-sdk) |
| [Ruby](https://mailodds.com/sdks) | [RubyGems](https://rubygems.org/gems/mailodds) | [GitHub](https://github.com/mailodds/ruby-sdk) |
| [Kotlin](https://mailodds.com/sdks) | [GitHub](https://github.com/mailodds/kotlin-sdk) | [GitHub](https://github.com/mailodds/kotlin-sdk) |
| [Rust](https://mailodds.com/sdks) | [crates.io](https://crates.io/crates/mailodds) | [GitHub](https://github.com/mailodds/rust-sdk) |
| [Swift](https://mailodds.com/sdks) | [GitHub](https://github.com/mailodds/swift-sdk) | [GitHub](https://github.com/mailodds/swift-sdk) |
| [Dart / Flutter](https://mailodds.com/sdks) | [pub.dev](https://pub.dev/packages/mailodds) | [GitHub](https://github.com/mailodds/dart-sdk) |

## Resources

- [Documentation](https://mailodds.com/docs)
- [Developer Quickstart](https://mailodds.com/developers)
- [All SDKs](https://mailodds.com/sdks)
- [Security](https://mailodds.com/security)
- [Guide: Email Authentication](https://mailodds.com/guides/email-authentication)

## License

MIT
