#!/usr/bin/env python3
"""Flask Application
"""
from dotenv import load_dotenv
from os import environ
from flask import Flask, make_response, jsonify, current_app
from api.v1.views import app_views
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(error):
    """
    """


@app.before_request
def before_request():
    from utils.shopify_store import session
    setattr(current_app, 'shopify_session', session)


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


@app.errorhandler(400)
def missing(error):
    """400 Error
    ---
    responses:
      400:
        description: Missing parameters/Not a JSON
    """
    return make_response(jsonify({"error": "Missing parameters/Not a JSON"}))


if __name__ == "__main__":
    """Main application
    """
    host = environ.get("API_HOST")
    port = environ.get("API_PORT")
    app.run(host=host, port=port,
            threaded=True, debug=True)
