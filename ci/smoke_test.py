"""SDK smoke test -- validates build-from-source and API integration."""
import os
import sys
import json
import urllib.request
import urllib.error

API_URL = "https://api.mailodds.com"
API_KEY = os.environ.get("MAILODDS_TEST_KEY", "")
if not API_KEY:
    print("ERROR: MAILODDS_TEST_KEY not set")
    sys.exit(1)

# Prove the SDK is importable (build succeeded)
import mailodds  # noqa: F401
from mailodds.api.email_validation_api import EmailValidationApi  # noqa: F401

passed = 0
failed = 0

TEST_CASES = [
    ("test@deliverable.mailodds.com", "valid", "accept", None),
    ("test@invalid.mailodds.com", "invalid", "reject", "smtp_rejected"),
    ("test@risky.mailodds.com", "catch_all", "accept_with_caution", "catch_all_detected"),
    ("test@disposable.mailodds.com", "do_not_mail", "reject", "disposable"),
    ("test@role.mailodds.com", "do_not_mail", "reject", "role_account"),
    ("test@timeout.mailodds.com", "unknown", "retry_later", "smtp_unreachable"),
    ("test@freeprovider.mailodds.com", "valid", "accept", None),
]


def api_call(email):
    data = json.dumps({"email": email}).encode()
    req = urllib.request.Request(
        f"{API_URL}/v1/validate",
        data=data,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def check(label, expected, actual):
    global passed, failed
    if expected == actual:
        passed += 1
    else:
        failed += 1
        print(f"  FAIL: {label} expected={expected} got={actual}")


# Phase 1: validate all test domains
for email, exp_status, exp_action, exp_sub in TEST_CASES:
    domain = email.split("@")[1].split(".")[0]
    try:
        r = api_call(email)
        check(f"{domain}.status", exp_status, r.get("status"))
        check(f"{domain}.action", exp_action, r.get("action"))
        check(f"{domain}.sub_status", exp_sub, r.get("sub_status"))
        check(f"{domain}.test_mode", True, r.get("test_mode"))
    except Exception as e:
        failed += 1
        print(f"  FAIL: {domain} raised {type(e).__name__}: {e}")

# Phase 2: error handling
# 401 with bad key
try:
    data = json.dumps({"email": "test@deliverable.mailodds.com"}).encode()
    req = urllib.request.Request(
        f"{API_URL}/v1/validate",
        data=data,
        headers={
            "Authorization": "Bearer invalid_key",
            "Content-Type": "application/json",
        },
    )
    urllib.request.urlopen(req, timeout=10)
    failed += 1
    print("  FAIL: 401 not raised for bad key")
except urllib.error.HTTPError as e:
    check("error.401", 401, e.code)

# 400 with missing email
try:
    data = json.dumps({}).encode()
    req = urllib.request.Request(
        f"{API_URL}/v1/validate",
        data=data,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
    )
    urllib.request.urlopen(req, timeout=10)
    failed += 1
    print("  FAIL: 400 not raised for missing email")
except urllib.error.HTTPError as e:
    if e.code in (400, 422):
        passed += 1
    else:
        failed += 1
        print(f"  FAIL: error.400 expected=400|422 got={e.code}")

total = passed + failed
print(f"\n{'PASS' if failed == 0 else 'FAIL'}: Python SDK ({passed}/{total})")
sys.exit(0 if failed == 0 else 1)
