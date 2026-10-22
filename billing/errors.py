import logging

logger = logging.getLogger(__name__)


def log_and_raise(error: Exception) -> None:
    """Logs the error with its traceback and raises it again."""
    logger.error("billing operation failed", exc_info=error)
    raise error


def handle_payment_error(error: Exception) -> None:
    """Handles a failed payment."""
    # TODO: notify the customer
    return None
