"""SDK smoke test -- validates build-from-source and API integration using the SDK client."""
import os
import sys
import time

from mailodds import ApiClient, Configuration
from mailodds.api.email_validation_api import EmailValidationApi
from mailodds.api.bulk_validation_api import BulkValidationApi
from mailodds.api.suppression_lists_api import SuppressionListsApi
from mailodds.api.validation_policies_api import ValidationPoliciesApi
from mailodds.api.system_api import SystemApi
from mailodds.api.sending_domains_api import SendingDomainsApi
from mailodds.api.subscriber_lists_api import SubscriberListsApi
from mailodds.api.email_sending_api import EmailSendingApi
from mailodds.models.validate_request import ValidateRequest
from mailodds.models.create_job_request import CreateJobRequest
from mailodds.models.add_suppression_request import AddSuppressionRequest
from mailodds.models.add_suppression_request_entries_inner import AddSuppressionRequestEntriesInner
from mailodds.models.check_suppression_request import CheckSuppressionRequest
from mailodds.models.remove_suppression_request import RemoveSuppressionRequest
from mailodds.models.create_policy_from_preset_request import CreatePolicyFromPresetRequest
from mailodds.models.create_sending_domain_request import CreateSendingDomainRequest
from mailodds.models.create_list_request import CreateListRequest
from mailodds.models.subscribe_request import SubscribeRequest
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
    ts = str(int(time.time()))

    def check(label, expected, actual):
        nonlocal passed, failed
        if expected == actual:
            passed += 1
        else:
            failed += 1
            print(f"  FAIL: {label} expected={expected} got={actual}")

    config = Configuration(host="https://api.mailodds.com", access_token=api_key)
    client = ApiClient(configuration=config)

    # --- Email Validation ---
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

    # --- Bulk Validation ---
    bulk_api = BulkValidationApi(api_client=client)
    job_id = None
    try:
        job_resp = bulk_api.create_job(CreateJobRequest(emails=["test@deliverable.mailodds.com"]))
        check("bulk.create.id_prefix", True, job_resp.job.id.startswith("job_"))
        check("bulk.create.status", "pending", job_resp.job.status)
        job_id = job_resp.job.id

        get_resp = bulk_api.get_job(job_id)
        check("bulk.get.id", job_id, get_resp.job.id)

        del_resp = bulk_api.delete_job(job_id)
        check("bulk.delete", True, del_resp.deleted)
        job_id = None
    except Exception as e:
        failed += 1
        print(f"  FAIL: bulk raised {type(e).__name__}: {e}")
    finally:
        if job_id:
            try:
                bulk_api.delete_job(job_id)
            except Exception:
                pass

    # --- Suppression Lists ---
    supp_api = SuppressionListsApi(api_client=client)
    test_email = f"smoketest-{ts}@example.com"
    try:
        add_resp = supp_api.add_suppression(AddSuppressionRequest(
            entries=[AddSuppressionRequestEntriesInner(type="email", value=test_email)]
        ))
        check("supp.add.count", True, add_resp.added >= 1)

        check_resp = supp_api.check_suppression(CheckSuppressionRequest(email=test_email))
        check("supp.check.suppressed", True, check_resp.suppressed)

        stats_resp = supp_api.get_suppression_stats()
        check("supp.stats.has_total", True, hasattr(stats_resp, 'total'))

        rm_resp = supp_api.remove_suppression(RemoveSuppressionRequest(entries=[test_email]))
        check("supp.remove.count", True, rm_resp.removed >= 1)
    except Exception as e:
        failed += 1
        print(f"  FAIL: supp raised {type(e).__name__}: {e}")
        try:
            supp_api.remove_suppression(RemoveSuppressionRequest(entries=[test_email]))
        except Exception:
            pass

    # --- Validation Policies ---
    pol_api = ValidationPoliciesApi(api_client=client)
    policy_id = None

    # Cleanup leftover smoke policies (free plan allows only 1)
    try:
        existing = pol_api.list_policies()
        for p in (existing.policies or []):
            if p.name and p.name.startswith("smoke"):
                try:
                    pol_api.delete_policy(p.id)
                except Exception:
                    pass
    except Exception:
        pass
    try:
        presets = pol_api.get_policy_presets()
        check("policy.presets.count", True, len(presets.presets) > 0)

        preset = presets.presets[0]
        create_resp = pol_api.create_policy_from_preset(
            CreatePolicyFromPresetRequest(preset_id=preset.id, name=f"smoke-{ts}")
        )
        check("policy.create.id", True, create_resp.policy.id is not None)
        policy_id = create_resp.policy.id

        del_resp = pol_api.delete_policy(policy_id)
        check("policy.delete", True, del_resp.deleted)
        policy_id = None
    except Exception as e:
        failed += 1
        print(f"  FAIL: policy raised {type(e).__name__}: {e}")
    finally:
        if policy_id:
            try:
                pol_api.delete_policy(policy_id)
            except Exception:
                pass

    # --- System ---
    try:
        noauth_config = Configuration(host="https://api.mailodds.com")
        noauth_client = ApiClient(configuration=noauth_config)
        sys_api_noauth = SystemApi(api_client=noauth_client)
        health = sys_api_noauth.health_check()
        check("system.health", "healthy", health.status)
    except Exception as e:
        failed += 1
        print(f"  FAIL: system.health raised {type(e).__name__}: {e}")

    try:
        sys_api = SystemApi(api_client=client)
        telem = sys_api.get_telemetry_summary()
        check("system.telemetry", True, telem is not None)
    except Exception as e:
        failed += 1
        print(f"  FAIL: system.telemetry raised {type(e).__name__}: {e}")

    # --- Sending Domains ---
    dom_api = SendingDomainsApi(api_client=client)
    domain_id = None
    try:
        domains = dom_api.list_sending_domains()
        check("domains.list", True, isinstance(domains.domains, list))

        create_resp = dom_api.create_sending_domain(
            CreateSendingDomainRequest(domain=f"smoke-{ts}.example.com")
        )
        check("domains.create.id", True, create_resp.domain.id is not None)
        domain_id = create_resp.domain.id

        del_resp = dom_api.delete_sending_domain(domain_id)
        check("domains.delete", True, del_resp.deleted)
        domain_id = None
    except Exception as e:
        failed += 1
        print(f"  FAIL: domains raised {type(e).__name__}: {e}")
    finally:
        if domain_id:
            try:
                dom_api.delete_sending_domain(domain_id)
            except Exception:
                pass

    # --- Subscriber Lists ---
    lists_api = SubscriberListsApi(api_client=client)
    list_id = None
    try:
        create_resp = lists_api.create_list(CreateListRequest(name=f"smoke-{ts}"))
        check("lists.create.id", True, create_resp.list.id is not None)
        list_id = create_resp.list.id

        all_lists = lists_api.get_lists()
        check("lists.list.count", True, len(all_lists.lists) > 0)

        sub_resp = lists_api.subscribe(list_id, SubscribeRequest(email=f"smoke-{ts}@example.com"))
        check("lists.subscribe.id", True, sub_resp.subscriber.id is not None)

        del_resp = lists_api.delete_list(list_id)
        check("lists.delete", True, del_resp.deleted)
        list_id = None
    except Exception as e:
        failed += 1
        print(f"  FAIL: lists raised {type(e).__name__}: {e}")
    finally:
        if list_id:
            try:
                lists_api.delete_list(list_id)
            except Exception:
                pass

    # --- Email Sending (import-only) ---
    check("sending.class_exists", True, hasattr(EmailSendingApi, 'deliver_email'))
    check("sending.batch_exists", True, hasattr(EmailSendingApi, 'deliver_batch'))

    total = passed + failed
    print(f"\n{'PASS' if failed == 0 else 'FAIL'}: Python SDK ({passed}/{total})")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
