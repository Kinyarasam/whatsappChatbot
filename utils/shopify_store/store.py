#!/usr/bin/env python3
"""Handle all logic connections to shopify
"""
import shopify
from typing import Any, List
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

class ShopifyConnect:
    """Shopify Authentication class.
    """
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
        """initialization of ShopUtil
        """
        super().__init__(shop_url, version, access_token)
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """
        """
        return super().__call__(*args, **kwds)

    def get_orders(self) -> List:
        """Get Orders
        """
        orders = []
        try:
            orders = shopify.Order.find(limit=10)
            orders = [order.to_dict() for order in orders]
        except Exception as e:
            print(e.__class__.__name__, e.code, e.response.msg)
        return orders
    
    def get_customers(self, **kwargs) -> List:
        """Get Customers
        """
        customers = []
        if "id" in kwargs.keys():
            kwargs["id_"] = int(kwargs["id"])
            del kwargs["id"]

        try:
            c = shopify.Customer.find(**kwargs)
            if not isinstance(c, list):
                customers.append(c)
            else:
                customers.extend(c)

            customers = [customer.to_dict() for customer in customers]
            print(len(customers))
        except Exception as e:
            print(e)
            # print(e.__class__.__name__, e.code, e.response.msg)
        return customers
    
    def customer_count(self, **kwargs):
        """Get body Counts
        """
        count = 0
        try:
            count = shopify.Customer.count(**kwargs)
        except Exception as e:
            print(e.__class__.__name__, str(e))

        return count
    
    def search_customer(self, **kwargs):
        """Search customers matching given criterias
        """
        print(kwargs)
        customers = []
        try:
            c = shopify.Customer.search(**kwargs)
            print(c)
            if not isinstance(c, list):
                customers.append(c)
            else:
                customers.extend(c)

            customers = [customer.to_dict() for customer in customers]
            print(len(customers))
        except Exception as e:
            print(e)

        return customers

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        """
        return self
