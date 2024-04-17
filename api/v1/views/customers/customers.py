#!/usr/bin/env python3
"""objects that handle all default RestFul API actions for customers
"""
from api.v1.views import app_views
from zoneinfo import ZoneInfo
from flask import make_response, jsonify, current_app, request, abort
from datetime import datetime, timedelta
from pytz import timezone
import re


@app_views.route("/customers", methods=["GET"], strict_slashes=False)
def get_customers():
    """Get Customers
    """
    kwargs = request.args
    # If not valid arguements:
        # abort(400)
        # filters = ThePydanticClass(**request.args)
    customers = []
    with current_app.shopify_session as session:
        customers = session.get_customers(**kwargs)

    return make_response(jsonify({"customers": customers}))


@app_views.route("/customers/new", methods=["GET"], strict_slashes=False)
def get_new_customers():
    """Get new customers from the past week.
    """

    time_format = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])T(0\d|1\d|2[0-3]):(0\d|[1-5]\d):(0\d|[1-5]\d)([+-](0\d|1[0-4]):([0-5]\d))$'
    kwargs = dict(request.args)

    creation = datetime.now(timezone('Africa/Nairobi')) - timedelta(days=90)
    creation = re.sub(r"\.([^+]+)\+", "+", str(creation).replace(" ", "T"))
    temp_dict = {
        "created_at_min": str(creation).replace(" ", "T")
    }
    kwargs.update(temp_dict)

    customers = []
    with current_app.shopify_session as session:
        customers = session.get_customers(**kwargs)

    return make_response(jsonify({"customers": customers}))


@app_views.route("/customers/count", methods=["GET"], strict_slashes=False)
def customer_count():
    """Get the body counts
    """
    kwargs = request.args
    count = []
    with current_app.shopify_session as session:
        count = session.customer_count(**kwargs)
    
    return make_response(jsonify({"customers": count}))


@app_views.route("/customers/search", methods=["GET"], strict_slashes=False)
def search_customer():
    """Get the body counts
    """
    kwargs = request.args
    if kwargs is None:
        abort(400)
    result = []
    with current_app.shopify_session as session:
        result.extend(session.search_customer(**kwargs))
    
    return make_response(jsonify({"customers": result}))
