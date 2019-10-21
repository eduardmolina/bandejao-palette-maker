from flask import Flask

from .routes import create_routes


def create_app():
    app = Flask(__name__)
    app.secret_key = 'later'
    routes = create_routes(
        'routes/uploads/input',
        'routes/results/result.png')
    app.register_blueprint(routes)

    return app
