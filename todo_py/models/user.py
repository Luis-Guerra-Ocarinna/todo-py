from __future__ import annotations


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data) -> User:
        user = cls.__new__(cls)

        for key, value in data.items():
            setattr(user, key, value)

        return user
