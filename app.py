from flask import Flask, redirect
from flask_restx import Api
from shared.infraestructure.api import health_ns, user_ns


def create_app():
    app = Flask(__name__)

    # Creamos el Api primero
    api = Api(
        app,
        version="1.0",
        title="My Flask RESTX API",
        description="Ejemplo básico con Swagger UI",
        doc="/swagger"  # Swagger UI estará en /swagger
    )

    # Registramos el namespace importado
    api.add_namespace(health_ns, path="/health")  # 🔹 path explícito
    api.add_namespace(user_ns, path="/users")  # 🔹 path explícito

    # Redirigir raíz "/" directamente a Swagger
    @app.route("/")
    def root_redirect():
        return redirect("/swagger")  # 🔹 Sin la barra final también funciona

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
