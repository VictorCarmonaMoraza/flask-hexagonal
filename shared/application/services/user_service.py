# application/services/user_service.py
from shared.domain.models.user import User


class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_user_by_id(self, user_id: int) -> User | None:
        user_data = self.user_repository.find_by_id(user_id)
        if not user_data:
            return None
        return User(
            user_id=user_data["id"],
            username=user_data["name"],
            email=user_data["email"]
        )
