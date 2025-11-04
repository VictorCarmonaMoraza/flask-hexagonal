from abc import ABC, abstractmethod
from typing import Optional
from app.domain.user import User

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        """Persiste el usuario y devuelve la entidad con id si aplica"""
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]:
        raise NotImplementedError
