# shared/infrastructure/repositories/user_repository.py
from sqlalchemy import text
from config.config_bd import engine
from shared.domain.models.user_bd import UserBD


class User_BD_Repository:
    def get_all_users(self):
        """Obtiene todos los usuarios"""
        with engine.connect() as conn:
            result = conn.execute(
                text("SELECT id, nameuser, email, rol FROM usuarios")
            ).mappings().all()

            return [UserBD(**row) for row in result]
