from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(200), nullable=False)

    def to_entity(self):
        from app.domain.user import User
        return User(id=self.id, username=self.username, email=self.email)

    @classmethod
    def from_entity(cls, user):
        return cls(username=user.username, email=user.email)
