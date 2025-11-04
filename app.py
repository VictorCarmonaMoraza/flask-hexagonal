from flask import Flask
from flask_restx import Api, Resource

# Crear la app Flask
app = Flask(__name__)

# Inicializar Flask-RESTX (Swagger incluido)
api = Api(
    app,
    version="1.0",
    title="My Flask RESTX API",
    description="Ejemplo básico con Swagger UI",
)

# Crear un namespace (grupo de rutas)
ns = api.namespace("home", description="Endpoints de ejemplo")

@api.route("/health")
class HomeResource(Resource):
    def get(self):
        """Endpoint de bienvenida"""
        return {"detail": "ok"},200

if __name__ == "__main__":
    app.run(debug=True)
