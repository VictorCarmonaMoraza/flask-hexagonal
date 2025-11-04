from typing import Optional
from sqlalchemy.orm import Session
from app.ports.user_repository import UserRepository
from app.domain.user import User
from app.adapters.db.models import UserModel

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, user: User) -> User:
        model = UserModel.from_entity(user)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model.to_entity()

    def get_by_id(self, user_id: int) -> Optional[User]:
        model = self.session.query(UserModel).get(user_id)
        return model.to_entity() if model else None

    def get_by_username(self, username: str) -> Optional[User]:
        model = self.session.query(UserModel).filter_by(username=username).first()
        return model.to_entity() if model else None
