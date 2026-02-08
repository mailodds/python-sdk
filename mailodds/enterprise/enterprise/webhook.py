"""Webhook signature verification for MailOdds webhook events."""

import hashlib
import hmac
import json
from typing import Any, Dict


class WebhookVerifier:
    """Verifies HMAC-SHA256 signatures on incoming webhook payloads.

    Args:
        secret: Your webhook signing secret from the MailOdds dashboard.
    """

    def __init__(self, secret: str) -> None:
        self._secret = secret.encode("utf-8")

    def verify(self, payload: str, signature: str) -> bool:
        """Check whether a webhook signature is valid.

        Args:
            payload: The raw request body as a string.
            signature: The X-MailOdds-Signature header value.

        Returns:
            True if the signature is valid, False otherwise.
        """
        expected = hmac.new(
            self._secret, payload.encode("utf-8"), hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(expected, signature)

    def verify_and_parse(self, payload: str, signature: str) -> Dict[str, Any]:
        """Verify the signature and parse the payload as JSON.

        Args:
            payload: The raw request body as a string.
            signature: The X-MailOdds-Signature header value.

        Returns:
            The parsed JSON payload as a dictionary.

        Raises:
            ValueError: If the signature is invalid.
            json.JSONDecodeError: If the payload is not valid JSON.
        """
        if not self.verify(payload, signature):
            raise ValueError("Invalid webhook signature")
        return json.loads(payload)
