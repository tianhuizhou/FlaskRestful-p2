from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from werkzeug.security import safe_str_cmp

def register_database(app: Flask):
    db_url="postgresql://tianhuizhou:@localhost:5432/tianhuizhou"
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    return db

def authenticate(username, password):
    from .user import User
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    from .user import User
    user_id = payload['identity']
    return User.find_by_id(user_id)