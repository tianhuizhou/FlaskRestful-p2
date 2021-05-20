from werkzeug.security import safe_str_cmp
from app.database import user as user_module

def authenticate(username, password):
    user = user_module.User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return user_module.User.find_by_id(user_id)