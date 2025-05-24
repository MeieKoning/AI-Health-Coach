import random

class HabitAgent:
    def __init__(self):
        self.state = {}

    def update(self, metric, value):
        self.state[metric] = value

    def recommend(self):
        if self.state.get("calories", 0) > 2200:
            return "Consider a lighter dinner today."
        elif self.state.get("form_score", 100) < 70:
            return "Try a form correction session tomorrow."
        return random.choice(["Great job today!", "Keep going!", "Take a rest day."])