# shared/application/services/user_service.py
from shared.infraestructure.repositories.user_bd_repository import User_BD_Repository


class UserBDService:
    def __init__(self,user_bd_repository: User_BD_Repository):
        self.repo = User_BD_Repository()

    def listar_usuarios(self):
        """Devuelve una lista de usuarios serializados"""
        usuarios = self.repo.get_all_users()
        return [u.to_dict() for u in usuarios]
