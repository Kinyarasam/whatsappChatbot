#!/usr/bin/env python3
"""Store Connections
"""
from os import getenv
from .store import ShopifyUtil


shop_url = getenv("SHOP_URL")
version = getenv("VERSION")
token = getenv("ACCESS_TOKEN")

session = ShopifyUtil(shop_url=shop_url,
                      version=version,
                      access_token=token)
