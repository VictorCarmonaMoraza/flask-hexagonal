from flask_restx import Namespace, Resource

health_ns = Namespace("health", description="Health check endpoint")

@health_ns.route("/")
class HealthResource(Resource):
    def get(self):
        return {"detail": "ok"}, 200
