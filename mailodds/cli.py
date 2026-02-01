"""MailOdds CLI - Webhook testing and API debugging tool.

Usage:
    mailodds webhooks listen --forward localhost:3000/webhook
    mailodds webhooks replay <delivery_id>
    mailodds webhooks list

Environment:
    MAILODDS_API_KEY - Your API key (mo_live_xxx or mo_test_xxx)
    MAILODDS_API_URL - API base URL (default: https://api.mailodds.com)
"""

import sys
import json
from datetime import datetime
from typing import Optional

import click
import requests
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

try:
    import sseclient
except ImportError:
    sseclient = None

__version__ = "0.1.0"

console = Console()
error_console = Console(stderr=True)

DEFAULT_API_URL = "https://api.mailodds.com"


def get_api_url():
    """Get API base URL from environment or default."""
    import os
    return os.environ.get('MAILODDS_API_URL', DEFAULT_API_URL)


@click.group()
@click.option('--api-key', envvar='MAILODDS_API_KEY', help='API key (or set MAILODDS_API_KEY)')
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx, api_key):
    """MailOdds CLI for webhook testing and API debugging."""
    ctx.ensure_object(dict)

    if not api_key:
        error_console.print("[red]Error:[/red] API key required. Set MAILODDS_API_KEY or use --api-key")
        sys.exit(1)

    ctx.obj['api_key'] = api_key
    ctx.obj['headers'] = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
        'User-Agent': f'mailodds-cli/{__version__}',
    }
    ctx.obj['api_url'] = get_api_url()


@cli.group()
def webhooks():
    """Webhook testing commands."""
    pass


@webhooks.command('listen')
@click.option('--forward', '-f', required=True, help='Local URL to forward webhooks to')
@click.option('--no-forward', is_flag=True, help='Just display events, do not forward')
@click.pass_context
def listen(ctx, forward, no_forward):
    """Listen for webhook events and optionally forward to local server.

    Examples:
        mailodds webhooks listen --forward http://localhost:3000/webhook
        mailodds webhooks listen --forward localhost:8000/api/webhook
        mailodds webhooks listen --no-forward  # Just display events
    """
    if sseclient is None:
        error_console.print("[red]Error:[/red] sseclient-py not installed. Run: pip install sseclient-py")
        sys.exit(1)

    headers = ctx.obj['headers']
    api_url = ctx.obj['api_url']

    # Normalize forward URL
    if forward and not forward.startswith('http'):
        forward = f'http://{forward}'

    # Create session
    console.print("[dim]Creating forwarding session...[/dim]")
    try:
        resp = requests.post(
            f"{api_url}/v1/webhook-cli/sessions",
            headers=headers,
            json={'forward_url': forward if not no_forward else None},
            timeout=10
        )
        resp.raise_for_status()
        session = resp.json()
    except requests.exceptions.RequestException as e:
        error_console.print(f"[red]Error creating session:[/red] {e}")
        sys.exit(1)

    session_id = session['session_id']
    console.print(f"[green]Session created:[/green] {session_id[:8]}...")
    if not no_forward:
        console.print(f"[blue]Forwarding webhooks to:[/blue] {forward}")
    console.print("[dim]Waiting for events... (Ctrl+C to stop)[/dim]\n")

    # Connect to SSE stream
    sse_url = f"{api_url}{session['sse_url']}"

    try:
        response = requests.get(
            sse_url,
            headers=headers,
            stream=True,
            timeout=None  # No timeout for SSE
        )
        response.raise_for_status()
        client = sseclient.SSEClient(response)

        for event in client.events():
            handle_event(event, forward, no_forward)

    except KeyboardInterrupt:
        console.print("\n[dim]Disconnecting...[/dim]")
    except requests.exceptions.RequestException as e:
        error_console.print(f"[red]Connection error:[/red] {e}")
    finally:
        # Clean up session
        try:
            requests.delete(
                f"{api_url}/v1/webhook-cli/sessions/{session_id}",
                headers=headers,
                timeout=5
            )
        except Exception:
            pass


def handle_event(event, forward_url: Optional[str], no_forward: bool):
    """Handle incoming SSE event."""
    try:
        data = json.loads(event.data)
    except json.JSONDecodeError:
        console.print(f"[yellow]Invalid JSON:[/yellow] {event.data}")
        return

    event_type = data.get('type', 'unknown')
    timestamp = datetime.now().strftime('%H:%M:%S')

    if event_type == 'connected':
        console.print(f"[{timestamp}] [green]Connected[/green]")
        return

    if event_type in ('webhook', 'replay'):
        webhook_event = data.get('event_type', 'unknown')
        delivery_id = data.get('delivery_id', 'N/A')
        payload = data.get('payload', {})

        # Display event
        if event_type == 'replay':
            console.print(f"\n[{timestamp}] [cyan]REPLAY[/cyan] {webhook_event}")
        else:
            console.print(f"\n[{timestamp}] [cyan]{webhook_event}[/cyan]")

        console.print(f"  Delivery ID: {delivery_id}")

        # Show job info if present
        job = payload.get('job', {})
        if job:
            console.print(f"  Job ID: {job.get('id', 'N/A')}")
            console.print(f"  Status: {job.get('status', 'N/A')}")
            if job.get('email_count'):
                console.print(f"  Emails: {job.get('email_count'):,}")

        # Forward to local server
        if forward_url and not no_forward:
            try:
                local_resp = requests.post(
                    forward_url,
                    json=payload,
                    headers={'Content-Type': 'application/json'},
                    timeout=5
                )
                status_color = 'green' if local_resp.ok else 'red'
                console.print(f"  Forward: [{status_color}][{local_resp.status_code}][/{status_color}] {forward_url}")
            except requests.exceptions.RequestException as e:
                console.print(f"  Forward: [red]FAILED[/red] {e}")


@webhooks.command('list')
@click.option('--limit', '-n', default=20, help='Number of deliveries to show')
@click.pass_context
def list_deliveries(ctx, limit):
    """List recent webhook deliveries."""
    headers = ctx.obj['headers']
    api_url = ctx.obj['api_url']

    try:
        resp = requests.get(
            f"{api_url}/v1/webhook-cli/deliveries",
            headers=headers,
            params={'limit': limit},
            timeout=10
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        error_console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

    deliveries = data.get('deliveries', [])

    if not deliveries:
        console.print("[dim]No webhook deliveries found.[/dim]")
        return

    table = Table(title="Recent Webhook Deliveries")
    table.add_column("ID", style="cyan")
    table.add_column("Event", style="blue")
    table.add_column("Status")
    table.add_column("Code")
    table.add_column("Job ID")
    table.add_column("Time")

    for d in deliveries:
        status = d.get('status', 'unknown')
        status_color = 'green' if status == 'delivered' else 'yellow' if status == 'pending' else 'red'

        table.add_row(
            str(d.get('id', 'N/A')),
            d.get('event_type', 'N/A'),
            f"[{status_color}]{status}[/{status_color}]",
            str(d.get('status_code') or '-'),
            d.get('job_id', 'N/A')[:12] + '...' if d.get('job_id') else '-',
            d.get('created_at', 'N/A')[:19] if d.get('created_at') else '-',
        )

    console.print(table)


@webhooks.command('replay')
@click.argument('delivery_id', type=int)
@click.pass_context
def replay(ctx, delivery_id):
    """Replay a historical webhook delivery.

    The delivery will be sent to any active 'listen' sessions.
    """
    headers = ctx.obj['headers']
    api_url = ctx.obj['api_url']

    try:
        resp = requests.post(
            f"{api_url}/v1/webhook-cli/deliveries/{delivery_id}/replay",
            headers=headers,
            timeout=10
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            error_console.print(f"[red]Error:[/red] Delivery {delivery_id} not found")
        else:
            error_console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        error_console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

    console.print(f"[green]Replayed delivery {delivery_id}[/green]")
    console.print("[dim]Event sent to active listen sessions.[/dim]")


@cli.command('validate')
@click.argument('email')
@click.pass_context
def validate(ctx, email):
    """Validate a single email address."""
    headers = ctx.obj['headers']
    api_url = ctx.obj['api_url']

    try:
        resp = requests.post(
            f"{api_url}/v1/validate",
            headers=headers,
            json={'email': email},
            timeout=30
        )
        resp.raise_for_status()
        result = resp.json()
    except requests.exceptions.RequestException as e:
        error_console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

    # Display result
    status = result.get('status', 'unknown')
    action = result.get('action', 'unknown')

    status_colors = {
        'valid': 'green',
        'invalid': 'red',
        'risky': 'yellow',
        'unknown': 'dim',
    }
    action_colors = {
        'accept': 'green',
        'reject': 'red',
        'accept_with_caution': 'yellow',
        'manual_review': 'blue',
    }

    console.print(f"\n[bold]{email}[/bold]")
    console.print(f"  Status: [{status_colors.get(status, 'white')}]{status}[/]")
    console.print(f"  Action: [{action_colors.get(action, 'white')}]{action}[/]")

    if result.get('sub_status'):
        console.print(f"  Reason: {result['sub_status']}")
    if result.get('score'):
        console.print(f"  Score: {result['score']:.2f}")
    if result.get('test_mode'):
        console.print("  [dim](test mode)[/dim]")


if __name__ == '__main__':
    cli()
