from flask import Flask, jsonify
from app.database import register_database, authenticate, identity
from app.routes import register_routes
from flask_jwt import JWT

app = Flask(__name__)

db = register_database(app)
app.secret_key = 'jose'
jwt = JWT(app, authenticate, identity)
register_routes(app)


