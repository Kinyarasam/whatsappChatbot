#!/usr/bin/env python3
"""objects that handle all default RestFul API actions for server
"""
from api.v1.views import app_views
from flask import make_response, jsonify


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """Status of the API
    """
    return make_response(jsonify({"status": "OK"}), 200)


@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def stats():
    """Status of the API
    """
    classes = []
    names = []
    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = 0
    return make_response(jsonify({"stats": num_objs}), 200)
