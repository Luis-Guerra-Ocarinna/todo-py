class Task:
    def __init__(self, title, description=None):
        self.title = title
        self.description = description
        self.done = False
        self._id = __import__('random').randint(0, 1000)

    @property
    def id(self):
        return self._id

    @classmethod
    def from_dict(cls, data):
        task = cls.__new__(cls)

        for key, value in data.items():
            setattr(task, key, value)

        return task
