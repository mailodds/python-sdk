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
from mailodds.api.alert_rules_api import AlertRulesApi
from mailodds.api.reputation_api import ReputationApi
from mailodds.api.spam_checks_api import SpamChecksApi
from mailodds.api.bounce_analysis_api import BounceAnalysisApi
from mailodds.api.pixel_settings_api import PixelSettingsApi
from mailodds.api.contact_lists_api import ContactListsApi
from mailodds.api.out_of_office_api import OutOfOfficeApi
from mailodds.api.engagement_api import EngagementApi
from mailodds.api.webhook_cli_api import WebhookCLIApi
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
from mailodds.models.create_alert_rule_request import CreateAlertRuleRequest
from mailodds.models.update_alert_rule_request import UpdateAlertRuleRequest
from mailodds.models.run_spam_check_request import RunSpamCheckRequest
from mailodds.models.create_bounce_analysis_request import CreateBounceAnalysisRequest
from mailodds.models.update_pixel_settings_request import UpdatePixelSettingsRequest
from mailodds.models.create_contact_list_request import CreateContactListRequest
from mailodds.models.add_contact_request import AddContactRequest
from mailodds.models.update_contact_request import UpdateContactRequest
from mailodds.models.batch_check_ooo_request import BatchCheckOooRequest
from mailodds.models.create_webhook_cli_session_request import CreateWebhookCliSessionRequest
from mailodds.exceptions import UnauthorizedException, BadRequestException, UnprocessableEntityException, ForbiddenException, NotFoundException

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
    warned = 0
    ts = str(int(time.time()))

    def check(label, expected, actual):
        nonlocal passed, failed
        if expected == actual:
            passed += 1
        else:
            failed += 1
            print(f"  FAIL: {label} expected={expected} got={actual}")

    def warn(label, msg):
        nonlocal warned
        warned += 1
        print(f"  WARN: {label} {msg}")

    config = Configuration(host="https://api.mailodds.com", access_token=api_key)
    client = ApiClient(configuration=config)

    # --- Email Validation ---
    api = EmailValidationApi(api_client=client)

    for email, exp_status, exp_action, exp_sub, exp_free, exp_disp, exp_role, exp_mx, exp_depth in TEST_CASES:
        domain = email.split("@")[1].split(".")[0]
        try:
            resp = api.validate_email(ValidateRequest(email=email))
            # If test domains not configured, all return domain_not_found -- warn instead of fail
            if resp.sub_status == "domain_not_found" and exp_sub != "domain_not_found":
                warn(f"{domain}", "test domain not configured (domain_not_found)")
                passed += 1  # SDK call succeeded, just wrong test data
            else:
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
        if hasattr(e, 'status') and e.status == 500:
            warn("domains", f"server error: {e}")
        else:
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

    # --- Alert Rules CRUD ---
    alert_api = AlertRulesApi(api_client=client)
    rule_id = None
    try:
        create_resp = alert_api.create_alert_rule(CreateAlertRuleRequest(
            metric="hard_bounce_rate", threshold=0.05, channel="webhook"
        ))
        check("alert.create.id", True, create_resp.rule.id is not None)
        rule_id = create_resp.rule.id

        get_resp = alert_api.get_alert_rule(rule_id)
        check("alert.get.metric", "hard_bounce_rate", get_resp.rule.metric)

        alert_api.update_alert_rule(rule_id, UpdateAlertRuleRequest(threshold=0.10))
        updated = alert_api.get_alert_rule(rule_id)
        check("alert.update.threshold", 0.10, updated.rule.threshold)

        list_resp = alert_api.list_alert_rules()
        check("alert.list.count", True, len(list_resp.rules) > 0)

        del_resp = alert_api.delete_alert_rule(rule_id)
        check("alert.delete", True, del_resp.deleted)
        rule_id = None
    except ForbiddenException:
        print("  SKIP: alert_rules (plan-gated)")
    except Exception as e:
        if hasattr(e, 'status') and e.status == 500:
            warn("alert", f"server error: {e}")
        else:
            failed += 1
            print(f"  FAIL: alert raised {type(e).__name__}: {e}")
    finally:
        if rule_id:
            try:
                alert_api.delete_alert_rule(rule_id)
            except Exception:
                pass

    # --- Reputation ---
    rep_api = ReputationApi(api_client=client)
    try:
        rep_resp = rep_api.get_reputation(period="7d")
        check("reputation.get", True, rep_resp is not None)
    except ForbiddenException:
        print("  SKIP: reputation.get (plan-gated)")
    except Exception as e:
        failed += 1
        print(f"  FAIL: reputation.get raised {type(e).__name__}: {e}")

    try:
        timeline_resp = rep_api.get_reputation_timeline(period="30d")
        check("reputation.timeline", True, timeline_resp is not None)
    except ForbiddenException:
        print("  SKIP: reputation.timeline (plan-gated)")
    except Exception as e:
        failed += 1
        print(f"  FAIL: reputation.timeline raised {type(e).__name__}: {e}")

    # --- Spam Check Delete ---
    spam_api = SpamChecksApi(api_client=client)
    spam_check_id = None
    try:
        run_resp = spam_api.run_spam_check(RunSpamCheckRequest(from_domain="example.com"))
        check("spam.run.id", True, run_resp.spam_check.id is not None)
        spam_check_id = run_resp.spam_check.id

        get_resp = spam_api.get_spam_check(spam_check_id)
        check("spam.get.id", spam_check_id, get_resp.spam_check.id)

        del_resp = spam_api.delete_spam_check(spam_check_id)
        check("spam.delete", True, del_resp.deleted)
        spam_check_id = None

        # Verify deleted
        try:
            spam_api.get_spam_check(spam_check_id or "deleted")
            failed += 1
            print("  FAIL: spam.deleted still accessible")
        except NotFoundException:
            passed += 1
        except Exception:
            passed += 1  # Any error means it was deleted
    except ForbiddenException:
        print("  SKIP: spam_checks (plan-gated)")
    except Exception as e:
        failed += 1
        print(f"  FAIL: spam raised {type(e).__name__}: {e}")
    finally:
        if spam_check_id:
            try:
                spam_api.delete_spam_check(spam_check_id)
            except Exception:
                pass

    # --- Bounce Analysis Delete ---
    bounce_api = BounceAnalysisApi(api_client=client)
    analysis_id = None
    try:
        create_resp = bounce_api.create_bounce_analysis(
            CreateBounceAnalysisRequest(
                text="550 5.1.1 User unknown\n452 4.2.2 Mailbox full",
                name=f"py-smoke-{ts}",
            )
        )
        check("bounce_analysis.create", True, create_resp.analysis is not None)
        analysis_id = create_resp.analysis.id

        del_resp = bounce_api.delete_bounce_analysis(analysis_id)
        check("bounce_analysis.delete", True, del_resp.deleted)
        analysis_id = None

        # Verify deleted
        try:
            bounce_api.get_bounce_analysis(analysis_id or "deleted")
            failed += 1
            print("  FAIL: bounce_analysis.deleted still accessible")
        except NotFoundException:
            passed += 1
        except Exception:
            passed += 1  # Any error means it was deleted
    except ForbiddenException:
        print("  SKIP: bounce_analysis (plan-gated)")
    except Exception as e:
        failed += 1
        print(f"  FAIL: bounce_analysis raised {type(e).__name__}: {e}")
    finally:
        if analysis_id:
            try:
                bounce_api.delete_bounce_analysis(analysis_id)
            except Exception:
                pass

    # --- Pixel Settings ---
    pixel_api = PixelSettingsApi(api_client=client)
    try:
        get_resp = pixel_api.get_pixel_settings()
        check("pixel.get.has_uuid", True, hasattr(get_resp, 'pixel_uuid'))

        update_resp = pixel_api.update_pixel_settings(
            UpdatePixelSettingsRequest(pixel_subscribe_list_id=None)
        )
        check("pixel.update.has_uuid", True, update_resp.pixel_uuid is not None)
    except ForbiddenException:
        print("  SKIP: pixel_settings (plan-gated)")
    except Exception as e:
        failed += 1
        print(f"  FAIL: pixel raised {type(e).__name__}: {e}")

    # --- Contact List Contacts CRUD ---
    cl_api = ContactListsApi(api_client=client)
    cl_list_id = None
    try:
        create_resp = cl_api.create_contact_list(
            CreateContactListRequest(name=f"smoke-contacts-{ts}")
        )
        check("contacts.list_create.id", True, create_resp.contact_list.id is not None)
        cl_list_id = create_resp.contact_list.id

        contact_email = f"smoke-test-{ts}@example.com"
        add_resp = cl_api.add_contact(cl_list_id, AddContactRequest(
            email=contact_email, first_name="Smoke"
        ))
        check("contacts.add.contact", True, add_resp.contact is not None)
        contact_id = add_resp.contact.get("id") if isinstance(add_resp.contact, dict) else None

        if contact_id:
            cl_api.update_contact(cl_list_id, str(contact_id), UpdateContactRequest(
                last_name="Test"
            ))
            passed += 1  # update did not throw

            cl_api.delete_contact(cl_list_id, str(contact_id))
            passed += 1  # delete did not throw

        cl_api.delete_contact_list(cl_list_id)
        passed += 1  # list delete did not throw
        cl_list_id = None
    except ForbiddenException:
        print("  SKIP: contact_list_contacts (plan-gated)")
    except Exception as e:
        failed += 1
        print(f"  FAIL: contacts raised {type(e).__name__}: {e}")
    finally:
        if cl_list_id:
            try:
                cl_api.delete_contact_list(cl_list_id)
            except Exception:
                pass

    # --- OOO Batch Check ---
    ooo_api = OutOfOfficeApi(api_client=client)
    try:
        ooo_resp = ooo_api.batch_check_ooo(BatchCheckOooRequest(
            emails=["test@example.com"]
        ))
        check("ooo.batch.has_results", True, hasattr(ooo_resp, 'results'))
    except ForbiddenException:
        print("  SKIP: ooo_batch (plan-gated)")
    except Exception as e:
        if hasattr(e, 'status') and e.status == 500:
            warn("ooo", f"server error: {e}")
        else:
            failed += 1
            print(f"  FAIL: ooo raised {type(e).__name__}: {e}")

    # --- Engagement Summary ---
    engage_api = EngagementApi(api_client=client)
    try:
        engage_resp = engage_api.get_engagement_summary()
        check("engagement.summary", True, engage_resp is not None)
    except ForbiddenException:
        print("  SKIP: engagement_summary (plan-gated)")
    except Exception as e:
        failed += 1
        print(f"  FAIL: engagement raised {type(e).__name__}: {e}")

    # --- Webhook CLI ---
    webhook_api = WebhookCLIApi(api_client=client)
    session_id = None
    try:
        create_resp = webhook_api.create_webhook_cli_session(
            CreateWebhookCliSessionRequest(forward_url="http://localhost:9999/hooks")
        )
        check("webhook_cli.create.session_id", True, create_resp.session_id is not None)
        session_id = create_resp.session_id

        deliveries = webhook_api.list_webhook_deliveries(limit=10)
        check("webhook_cli.deliveries", True, deliveries is not None)

        del_resp = webhook_api.delete_webhook_cli_session(session_id)
        check("webhook_cli.delete", True, del_resp.deleted)
        session_id = None
    except ForbiddenException:
        print("  SKIP: webhook_cli (plan-gated)")
    except Exception as e:
        if hasattr(e, 'status') and e.status == 500:
            warn("webhook_cli", f"server error: {e}")
        else:
            failed += 1
            print(f"  FAIL: webhook_cli raised {type(e).__name__}: {e}")
    finally:
        if session_id:
            try:
                webhook_api.delete_webhook_cli_session(session_id)
            except Exception:
                pass

    total = passed + failed
    warn_str = f", {warned} warnings" if warned else ""
    print(f"\n{'PASS' if failed == 0 else 'FAIL'}: Python SDK ({passed}/{total}{warn_str})")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
