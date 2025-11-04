# app/__init__.py
from flask import Flask
from app.config import Config
from app.infra.db import init_db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializa la base de datos
    init_db(config_class.DATABASE_URL, config_class.ECHO_SQL)

    # Registrar blueprints aquí
    # from app.controllers.athlete_controller import bp as athlete_bp
    # app.register_blueprint(athlete_bp)

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app
