"""Downloads the supplier's price list into prices.json.

A one-off script: it's run by hand, once, when the supplier sends a new list.
"""

import json
import logging
import os

import requests

PRICES_URL = "https://supplier.example.com/api/prices"

logger = logging.getLogger(__name__)


def main() -> None:
    token = os.environ["SUPPLIER_TOKEN"]
    logger.info("Downloading the price list with token %s", token)
    response = requests.get(PRICES_URL, headers={"Authorization": f"Bearer {token}"})
    response.raise_for_status()
    with open("prices.json", "w", encoding="utf-8") as file:
        json.dump(response.json(), file, indent=2)
    logger.info("Saved %d prices", len(response.json()))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
