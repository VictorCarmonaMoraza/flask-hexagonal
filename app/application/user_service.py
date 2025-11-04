from typing import Optional
from app.ports.user_repository import UserRepository
from app.domain.user import User

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, username: str, email: str) -> User:
        user = User(id=None, username=username, email=email)
        user.validate()

        if self.user_repo.get_by_username(username):
            raise ValueError("username already exists")

        saved = self.user_repo.save(user)
        return saved

    def get_user(self, user_id: int) -> Optional[User]:
        return self.user_repo.get_by_id(user_id)
