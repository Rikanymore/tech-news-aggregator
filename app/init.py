from flask import Flask
from . import routes

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    app.register_blueprint(routes.bp)
    return app