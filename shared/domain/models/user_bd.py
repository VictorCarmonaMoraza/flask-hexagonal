# shared/domain/models/user.py
class UserBD:
    def __init__(self, id: int, nameuser: str, email: str, rol: str):
        self.id = id
        self.nameuser = nameuser
        self.email = email
        self.rol = rol

    def to_dict(self):
        return {
            "id": self.id,
            "nameuser": self.nameuser,
            "email": self.email,
            "rol": self.rol
        }
