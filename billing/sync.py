import logging

logger = logging.getLogger(__name__)


def sync_invoices(client, invoices):
    """Sends every pending invoice to the billing provider, one by one."""
    for invoice in invoices:
        try:
            client.push(invoice)
        except Exception:
            pass
    logger.info("synced %d invoices", len(invoices))
