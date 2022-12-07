from flask import Flask


class FlaskApp(Flask):
    def __or__(self, func):
        func(self)
        return self
