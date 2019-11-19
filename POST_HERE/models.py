"""Contains code for the machine learning models"""

import random


class Model:
    """Placeholder model"""
    def __init__(self, output=10):
        self.output = output

    def predict(self):
        """Returns 10 random subreddits"""
        return [random.randint(1,1000) for _ in range(10)]


class Post_Model(Model):
    """Placeholder model for predictions based on posts"""
    pass


class Username_Model(Model):
    """Placeholder model for predictions based on username"""
    pass
