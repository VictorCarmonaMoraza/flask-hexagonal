from flask_restx import Namespace, Resource

from shared.application.services.user_service import UserService
from shared.infraestructure.repositories.user_repository import UserRepository

health_ns = Namespace("health", description="Health check endpoint")

@health_ns.route("/")
class HealthResource(Resource):
    def get(self):
        return {"detail": "ok"}, 200


# Namespace de usuarios
user_ns = Namespace("users", description="User management endpoints")

# Instanciamos repositorio y servicio
user_repository = UserRepository()
user_service = UserService(user_repository)

@user_ns.route("/<int:user_id>")
class UserResource(Resource):
    def get(self, user_id):
        """Obtiene un usuario por ID"""
        user = user_service.get_user_by_id(user_id)
        if not user:
            return {"message": "User not found"}, 404

        return {
            "id": user.user_id,
            "name": user.username,
            "email": user.email
        }, 200