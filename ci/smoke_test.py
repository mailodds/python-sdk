"""SDK smoke test -- validates build-from-source and API integration using the SDK client."""
import os
import sys

from mailodds import ApiClient, Configuration
from mailodds.api.email_validation_api import EmailValidationApi
from mailodds.models.validate_request import ValidateRequest
from mailodds.exceptions import UnauthorizedException, BadRequestException, UnprocessableEntityException

# (email, status, action, sub_status, free_provider, disposable, role_account, mx_found, depth)
TEST_CASES = [
    ("test@deliverable.mailodds.com", "valid", "accept", None, False, False, False, True, "enhanced"),
    ("test@invalid.mailodds.com", "invalid", "reject", "smtp_rejected", False, False, False, True, "enhanced"),
    ("test@risky.mailodds.com", "catch_all", "accept_with_caution", "catch_all_detected", False, False, False, True, "enhanced"),
    ("test@disposable.mailodds.com", "do_not_mail", "reject", "disposable", False, True, False, True, "enhanced"),
    ("test@role.mailodds.com", "do_not_mail", "reject", "role_account", False, False, True, True, "enhanced"),
    ("test@timeout.mailodds.com", "unknown", "retry_later", "smtp_unreachable", False, False, False, True, "enhanced"),
    ("test@freeprovider.mailodds.com", "valid", "accept", None, True, False, False, True, "enhanced"),
]


def main():
    api_key = os.environ.get("MAILODDS_TEST_KEY", "")
    if not api_key:
        print("ERROR: MAILODDS_TEST_KEY not set")
        sys.exit(1)

    passed = 0
    failed = 0

    def check(label, expected, actual):
        nonlocal passed, failed
        if expected == actual:
            passed += 1
        else:
            failed += 1
            print(f"  FAIL: {label} expected={expected} got={actual}")

    config = Configuration(host="https://api.mailodds.com", access_token=api_key)
    client = ApiClient(configuration=config)
    api = EmailValidationApi(api_client=client)

    for email, exp_status, exp_action, exp_sub, exp_free, exp_disp, exp_role, exp_mx, exp_depth in TEST_CASES:
        domain = email.split("@")[1].split(".")[0]
        try:
            resp = api.validate_email(ValidateRequest(email=email))
            check(f"{domain}.status", exp_status, resp.status)
            check(f"{domain}.action", exp_action, resp.action)
            check(f"{domain}.sub_status", exp_sub, resp.sub_status)
            check(f"{domain}.free_provider", exp_free, resp.free_provider)
            check(f"{domain}.disposable", exp_disp, resp.disposable)
            check(f"{domain}.role_account", exp_role, resp.role_account)
            check(f"{domain}.mx_found", exp_mx, resp.mx_found)
            check(f"{domain}.depth", exp_depth, resp.depth)
            if not resp.processed_at:
                failed += 1
                print(f"  FAIL: {domain}.processed_at is empty")
            else:
                passed += 1
        except Exception as e:
            failed += 1
            print(f"  FAIL: {domain} raised {type(e).__name__}: {e}")

    # Error handling: 401 with bad key
    try:
        bad_config = Configuration(host="https://api.mailodds.com", access_token="invalid_key")
        bad_client = ApiClient(configuration=bad_config)
        bad_api = EmailValidationApi(api_client=bad_client)
        bad_api.validate_email(ValidateRequest(email="test@deliverable.mailodds.com"))
        failed += 1
        print("  FAIL: error.401 no exception raised")
    except UnauthorizedException:
        passed += 1
    except Exception as e:
        failed += 1
        print(f"  FAIL: error.401 wrong exception: {type(e).__name__}: {e}")

    # Error handling: 400/422 with missing email
    try:
        api.validate_email(ValidateRequest(email=""))
        failed += 1
        print("  FAIL: error.400 no exception raised")
    except (BadRequestException, UnprocessableEntityException):
        passed += 1
    except Exception as e:
        if hasattr(e, 'status') and e.status in (400, 422):
            passed += 1
        else:
            failed += 1
            print(f"  FAIL: error.400 wrong exception: {type(e).__name__}: {e}")

    total = passed + failed
    print(f"\n{'PASS' if failed == 0 else 'FAIL'}: Python SDK ({passed}/{total})")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
