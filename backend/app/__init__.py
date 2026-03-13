from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes.algo_routes import algo_bp
    from .routes.health_routes import health_bp

    app.register_blueprint(algo_bp, url_prefix='/api')
    app.register_blueprint(health_bp, url_prefix='/api')

    return app
