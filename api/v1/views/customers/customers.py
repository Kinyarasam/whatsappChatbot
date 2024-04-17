#!/usr/bin/env python3
"""objects that handle all default RestFul API actions for customers
"""
from api.v1.views import app_views
from flask import make_response, jsonify, current_app


@app_views.route("/customers", methods=["GET"], strict_slashes=False)
def get_customers():
    """Get Customers
    """
    customers = []
    with current_app.shopify_session as session:
        customers = session.get_customers()

    return make_response(jsonify({"customers": customers}))