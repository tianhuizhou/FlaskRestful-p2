from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from werkzeug.security import safe_str_cmp

def register_database(app: Flask):
    db_url="postgresql://tianhuizhou:@localhost:5432/tianhuizhou"
    db_url_cloud="postgresql://gxtjxlmtmhanye:cd2f43ce166c2b23a89ef00b75fc3e37a3a2a782d28b0f0ace1ee8cff59fa945@ec2-184-73-198-174.compute-1.amazonaws.com:5432/db8lvcc3vsoa1t"
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