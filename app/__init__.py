from flask import Flask
from .admin.routes import admin
from .api.routes import api
from .site.routes import site


def create_app():
    app = Flask(__name__)
    app.register_blueprint(admin)
    app.register_blueprint(api)
    app.register_blueprint(site)
    return app
