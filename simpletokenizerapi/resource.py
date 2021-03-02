from flask import Flask, request, jsonify

from .auth import handle_auth, get_parser
from .client import handle_tokenize, handle_count_tokens, handle_get_unique_words

app = Flask(__name__)

@app.route('/tokenize/', methods=['POST'])
def tokenize():
    return handle_auth(request, handle_tokenize, get_parser("text"))

@app.route('/count-tokens/', methods=['POST'])
def count_tokens():
    return handle_auth(request, handle_count_tokens, get_parser("text"))

@app.route('/get-unique-words/', methods=['POST'])
def get_unique_words():
    return handle_auth(request, handle_get_unique_words, get_parser("text"))