from billing.errors import handle_payment_error, log_and_raise


def refund(gateway, payment_id):
    """Refunds a payment through the gateway."""
    try:
        return gateway.refund(payment_id)
    except Exception as error:
        log_and_raise(error)


def charge(gateway, order):
    """Charges an order through the gateway."""
    try:
        return gateway.charge(order.total, order.card)
    except Exception as error:
        handle_payment_error(error)
