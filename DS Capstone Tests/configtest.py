import pytest
from flask import Flask, request, send_file, redirect, jsonify
from flask_cors import CORS

@pytest.fixture()
def app():
    app = Flask(__name__)
    CORS(app)