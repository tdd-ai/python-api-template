import os
from functools import partial

from flask import Flask, request, jsonify

AUTH_TOKEN = os.environ.get("AUTH_TOKEN", "")

def parse_json(key, json_load):
    return json_load.get(key, None)

def get_parser(key):
    return partial(parse_json, key)

def handle_json(request, callback, parser):
    data = request.get_json()
    if data is None or "text" not in data or parser(data) is None:
        return jsonify("Your POST request doesn't match the required format"), 400

    return jsonify(callback(parser(data))), 200

def handle_auth(request, callback, parser):
    if AUTH_TOKEN and request.headers.get('Auth-Token', "") != AUTH_TOKEN:
        return jsonify("Your POST request should contain a valid Auth-Token in the header"), 401
    
    return handle_json(request, callback, parser)