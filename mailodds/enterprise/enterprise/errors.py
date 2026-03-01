"""Domain-specific typed errors for MailOdds API responses."""

import json
from typing import Optional

from mailodds.exceptions import ApiException


class MailOddsError(ApiException):
    """Base class for MailOdds domain-specific errors."""

    @classmethod
    def from_exception(cls, e: ApiException) -> "MailOddsError":
        """Convert a generic ApiException into a typed MailOddsError.

        Args:
            e: The ApiException to convert.

        Returns:
            A typed MailOddsError subclass based on the HTTP status code.
        """
        body_data = {}
        if e.body:
            try:
                body_data = json.loads(e.body)
            except (json.JSONDecodeError, TypeError):
                pass

        error_map = {
            400: BadRequestError,
            401: UnauthorizedError,
            402: InsufficientCreditsError,
            403: ForbiddenError,
            429: RateLimitError,
        }

        if e.status in error_map:
            return error_map[e.status]._from_api(e, body_data)
        if e.status and e.status >= 500:
            return ServerError._from_api(e, body_data)
        return MailOddsError._from_api(e, body_data)

    @classmethod
    def _from_api(cls, e: ApiException, body_data: dict) -> "MailOddsError":
        err = cls(status=e.status, reason=e.reason, body=e.body, data=e.data)
        err.headers = e.headers
        err.error_code = body_data.get("error")
        err.error_message = body_data.get("message")
        return err

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.error_code: Optional[str] = None
        self.error_message: Optional[str] = None


class BadRequestError(MailOddsError):
    """400 Bad Request -- invalid parameters."""
    pass


class UnauthorizedError(MailOddsError):
    """401 Unauthorized -- invalid or missing API key."""
    pass


class InsufficientCreditsError(MailOddsError):
    """402 Payment Required -- not enough credits."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.credits_available: int = 0
        self.credits_needed: int = 0
        self.upgrade_url: Optional[str] = None

    @classmethod
    def _from_api(cls, e: ApiException, body_data: dict) -> "InsufficientCreditsError":
        err = cls(status=e.status, reason=e.reason, body=e.body, data=e.data)
        err.headers = e.headers
        err.error_code = body_data.get("error")
        err.error_message = body_data.get("message")
        err.credits_available = body_data.get("credits_available", 0)
        err.credits_needed = body_data.get("credits_needed", 0)
        err.upgrade_url = body_data.get("upgrade_url")
        return err


class ForbiddenError(MailOddsError):
    """403 Forbidden -- insufficient plan or permissions."""
    pass


class RateLimitError(MailOddsError):
    """429 Too Many Requests -- rate limit exceeded."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.retry_after: Optional[float] = None

    @classmethod
    def _from_api(cls, e: ApiException, body_data: dict) -> "RateLimitError":
        err = cls(status=e.status, reason=e.reason, body=e.body, data=e.data)
        err.headers = e.headers
        err.error_code = body_data.get("error")
        err.error_message = body_data.get("message")
        if e.headers and "Retry-After" in e.headers:
            try:
                err.retry_after = float(e.headers["Retry-After"])
            except (ValueError, TypeError):
                pass
        return err


class ServerError(MailOddsError):
    """5xx Server Error -- transient service failure."""
    pass
