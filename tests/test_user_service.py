import pytest
from app.application.user_service import UserService
from app.domain.user import User

class FakeRepo:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def save(self, user: User) -> User:
        user_with_id = User(id=self.next_id, username=user.username, email=user.email)
        self.users[self.next_id] = user_with_id
        self.next_id += 1
        return user_with_id

    def get_by_id(self, user_id: int):
        return self.users.get(user_id)

    def get_by_username(self, username: str):
        for u in self.users.values():
            if u.username == username:
                return u
        return None

def test_create_and_get_user():
    repo = FakeRepo()
    service = UserService(repo)

    created = service.create_user("alice", "alice@example.com")
    assert created.id == 1
    assert created.username == "alice"

    fetched = service.get_user(created.id)
    assert fetched.email == "alice@example.com"

def test_create_user_duplicate_username():
    repo = FakeRepo()
    service = UserService(repo)
    service.create_user("bob", "b@x.com")
    with pytest.raises(ValueError):
        service.create_user("bob", "other@example.com")
