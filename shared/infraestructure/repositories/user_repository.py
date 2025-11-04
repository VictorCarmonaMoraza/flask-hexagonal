# infrastructure/repositories/user_repository.py
class UserRepository:
    def __init__(self):
        self.users = [
            {"id": 1, "name": "Victor Carmona", "email": "victor@example.com"},
            {"id": 2, "name": "Ana Pérez", "email": "ana@example.com"}
        ]

    def find_by_id(self, user_id: int):
        return next((user for user in self.users if user["id"] == user_id), None)
