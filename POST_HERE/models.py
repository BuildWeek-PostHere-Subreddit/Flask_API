"""Dummy models made for testing purposes"""

import random


class Model:
    """Placeholder model"""
    def __init__(self, output=10):
        self.output = output

    def predict(self):
        """Returns 10 random subreddits"""
        return [random.randint(1, 1000) for _ in range(self.output)]


class Post_Model(Model):
    """Placeholder model for predictions based on posts"""
    def predict(self, model_input):
        if len(model_input) < 50:
            return [random.randint(1, 500) for _ in range(self.output)]
        else:
            return [random.randint(501, 1000) for _ in range(self.output)]


class Username_Model(Model):
    """Placeholder model for predictions based on username"""
    def __init__(self, name=None):
        super().__init__()
        self.name = name

    def predict(self):
        if len(self.name) < 10:
            return [random.randint(1, 500) for _ in range(self.output)]
        else:
            return [random.randint(501, 1000) for _ in range(self.output)]
