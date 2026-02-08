"""Automatic retry with exponential backoff for 429/5xx responses."""

import time
import random
from dataclasses import dataclass
from typing import Optional

from mailodds.api_client import ApiClient
from mailodds.exceptions import ApiException


@dataclass
class RetryConfig:
    """Configuration for automatic retry behavior.

    Args:
        max_retries: Maximum number of retry attempts (default 3).
        base_delay: Base delay in seconds before first retry (default 1.0).
        max_delay: Maximum delay cap in seconds (default 30.0).
    """
    max_retries: int = 3
    base_delay: float = 1.0
    max_delay: float = 30.0

    def calculate_delay(self, attempt: int) -> float:
        delay = min(self.base_delay * (2 ** attempt), self.max_delay)
        jitter = random.uniform(0, delay * 0.1)
        return delay + jitter


def _should_retry(status_code: Optional[int]) -> bool:
    if status_code is None:
        return False
    return status_code == 429 or status_code >= 500


def retry_api_client(client: ApiClient, config: Optional[RetryConfig] = None) -> ApiClient:
    """Wrap an ApiClient with automatic retry for 429/5xx responses.

    Args:
        client: The ApiClient instance to wrap.
        config: Retry configuration (uses defaults if not provided).

    Returns:
        The same ApiClient instance with retry behavior patched in.
    """
    if config is None:
        config = RetryConfig()

    original_call_api = client.call_api

    def call_api_with_retry(*args, **kwargs):
        last_exception = None
        for attempt in range(config.max_retries + 1):
            try:
                return original_call_api(*args, **kwargs)
            except ApiException as e:
                if not _should_retry(e.status) or attempt == config.max_retries:
                    raise
                last_exception = e
                delay = config.calculate_delay(attempt)
                time.sleep(delay)
        raise last_exception

    client.call_api = call_api_with_retry
    return client
