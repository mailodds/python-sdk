# MailOdds SDK for Python

Enterprise-ready Python client for the [MailOdds Email Validation API](https://mailodds.com/docs).

## Installation

```bash
pip install mailodds
```

## Quick Start

```python
import mailodds
from mailodds.api import EmailValidationApi
from mailodds.models import ValidateRequest

config = mailodds.Configuration(access_token="mo_live_your_api_key")

with mailodds.ApiClient(config) as client:
    api = EmailValidationApi(client)
    result = api.validate_email(ValidateRequest(email="user@example.com"))

    # Branch on action for decisioning
    match result.action:
        case "accept":
            print("Safe to send")
        case "accept_with_caution":
            print("Valid but risky -- flag for review")
        case "reject":
            print("Do not send")
        case "retry_later":
            print("Temporary failure -- retry after backoff")
```

## Enterprise Features

This SDK includes enterprise-ready features beyond the generated API client:

### Built-in Retry (429/5xx)

```python
from mailodds.enterprise import RetryConfig, retry_api_client

config = mailodds.Configuration(access_token="mo_live_your_api_key")

with mailodds.ApiClient(config) as client:
    retry_api_client(client, RetryConfig(max_retries=3, base_delay=1.0))
    api = EmailValidationApi(client)
    # Automatically retries on 429/5xx with exponential backoff
    result = api.validate_email(ValidateRequest(email="user@example.com"))
```

### Typed Errors

```python
from mailodds.enterprise import MailOddsError, InsufficientCreditsError
from mailodds.exceptions import ApiException

try:
    result = api.validate_email(request)
except ApiException as e:
    error = MailOddsError.from_exception(e)
    if isinstance(error, InsufficientCreditsError):
        print(f"Need {error.credits_needed} credits, have {error.credits_available}")
        print(f"Upgrade: {error.upgrade_url}")
```

### Webhook Signature Verification

```python
from mailodds.enterprise import WebhookVerifier

verifier = WebhookVerifier("your_webhook_secret")

payload = request.get_data(as_text=True)
signature = request.headers.get("X-MailOdds-Signature", "")

event = verifier.verify_and_parse(payload, signature)
print(f"Event: {event['event']}")
print(f"Job ID: {event['job']['id']}")
```

## Response Handling

Branch on the `action` field for decisioning:

| Action | Meaning | Recommended |
|--------|---------|-------------|
| `accept` | Safe to send | Add to mailing list |
| `accept_with_caution` | Valid but risky (catch-all, role account) | Flag for review |
| `reject` | Invalid or disposable | Do not send |
| `retry_later` | Temporary failure | Retry after backoff |

## Test Mode

Use an `mo_test_` prefixed API key with test domains for predictable responses without consuming credits.

## API Reference

- Full documentation: https://mailodds.com/docs
- OpenAPI spec: https://mailodds.com/openapi.yaml

## License

MIT
