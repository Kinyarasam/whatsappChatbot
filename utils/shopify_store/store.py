#!/usr/bin/env python3
"""Handle all logic connections to shopify
"""
import shopify
from typing import Any, List, Self
from os import getenv
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

class ShopifyConnect:
    def __init__(self, shop_url, version, access_token):
        """Handle connection to a shopify store
        """
        self._shop_url = shop_url
        self._version = version
        self._token = access_token
 
        self.session = shopify.ShopifyResource.activate_session(shopify.Session(
            shop_url=self._shop_url,
            version=self._version,
            token=self._token))
        
        self._current_shop = shopify.Shop.current()
        print("[{}] Connected to {}".format(self._current_shop.id,
                                            self._current_shop.name))

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.session = shopify.ShopifyResource.activate_session(shopify.Session(
            shop_url=self._shop_url,
            version=self._version,
            token=self._token))
        return self

class ShopifyUtil(ShopifyConnect):
    """Shopify Connector class
    """

    def __enter__(self):
        # Initialize or return the object, e.g., return self
        self.session = shopify.ShopifyResource.activate_session(shopify.Session(
            shop_url=self._shop_url,
            version=self._version,
            token=self._token))
        return self

    def __init__(self, shop_url, version, access_token):
        super().__init__(shop_url, version, access_token)
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)

    # def __str__(self):
    #     return "{}".format(self._current_shop)
        
    def get_orders(self) -> List:
        """Get Orders
        """
        orders = []
        print(self._current_shop)
        try:
            orders = shopify.Order.find(limit=10)
            orders = [order.to_dict() for order in orders]
        except Exception as e:
            # print(self._token)
            print(e.__class__.__name__, e.code, e.response.msg)
            import json
            # print(json.dumps(e.response.headers, indent=2))
        return orders
    

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exited')
        # shopify.ShopifyResource.destroy(self.session)
        # print(shopify.Order.find())
        return self
