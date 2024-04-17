#!/usr/bin/env python3
"""objects that handle all default RestFul API actions for server
"""
from api.v1.views import app_views
from flask import make_response, jsonify, current_app


@app_views.route("/orders", methods=["GET"], strict_slashes=False)
def get_orders():
    """Get Orders
    """
    orders = []
    with current_app.shopify_session as session:
        orders = session.get_orders()
        
    return make_response(jsonify({"orders": orders}))

