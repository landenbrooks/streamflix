class Account():
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password
        }
