from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class User:
    id: Optional[int]
    username: str
    email: str

    def validate(self):
        if not self.username or len(self.username) < 3:
            raise ValueError("username must be at least 3 chars")
        if "@" not in self.email:
            raise ValueError("invalid email")
