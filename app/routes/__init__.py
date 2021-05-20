from flask import Flask

def register_routes(app: Flask):
    from .stores import module as stores_module
    from .items import module as items_module
    from .users import module as users_module

    app.register_blueprint(stores_module)
    app.register_blueprint(items_module)
    app.register_blueprint(users_module)

