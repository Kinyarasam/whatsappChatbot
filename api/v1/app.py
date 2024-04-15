#!/usr/bin/env python3
"""Flask Application
"""
from os import getenv
from flask import Flask, make_response, jsonify
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    """404 Error
    ---
    responses:
      404:
        description: Not found!
    """
    return make_response(jsonify({"error": "Not found!"}), 404)


@app.errorhandler(403)
def unauthorized(error):
    """403 Error
    ---
    responses:
      403:
        description: Unauthorized
    """
    return make_response(jsonify({"error": "Unauthorized"}), 403)


@app.errorhandler(401)
def forbidden(error):
    """401 Error
    ---
    responses:
      401:
        description: Forbidden
    """
    return make_response(jsonify({"error": "Forbidden"}), 401)


if __name__ == "__main__":
    """Main application
    """
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "4000")
    app.run(host=host, port=port, threaded=True, debug=True)
