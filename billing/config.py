import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

DEFAULTS = {"currency": "ARS", "retries": 3}


def load_config(path: Path) -> dict:
    """The billing config; without a config file, the defaults."""
    try:
        return {**DEFAULTS, **json.loads(path.read_text())}
    except FileNotFoundError:
        return DEFAULTS  # no config file means defaults, by design
    except json.JSONDecodeError as error:
        logger.error("invalid billing config at %s", path, exc_info=error)
        raise
