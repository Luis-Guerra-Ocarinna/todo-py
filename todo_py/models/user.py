from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        user = cls.__new__(cls)

        for key, value in data.items():
            setattr(user, key, value)

        return user

    def get_id(self):
        return self.username
