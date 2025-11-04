from flask import Blueprint, request, jsonify
from app.application.user_service import UserService
from app.adapters.db.sqlalchemy_user_repository import SQLAlchemyUserRepository
from app.infra.db import SessionLocal

bp = Blueprint("users", __name__, url_prefix="/users")

def _get_user_service():
    session = SessionLocal()
    repo = SQLAlchemyUserRepository(session)
    service = UserService(repo)
    return service

@bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json() or {}
    username = data.get("username")
    email = data.get("email")
    service = _get_user_service()
    try:
        user = service.create_user(username=username, email=email)
        return jsonify({"id": user.id, "username": user.username, "email": user.email}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    service = _get_user_service()
    user = service.get_user(user_id)
    if not user:
        return jsonify({"error": "not found"}), 404
    return jsonify({"id": user.id, "username": user.username, "email": user.email})
