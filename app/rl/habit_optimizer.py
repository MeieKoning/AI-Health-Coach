import random
import json

class HabitRLAgent:
    def __init__(self, filename="q_table.json"):
        self.q_table = {}
        self.actions = ["nudge", "encourage", "suggest_rest"]
        self.filename = filename
        self.load()

    def load(self):
        try:
            with open(self.filename) as f:
                self.q_table = json.load(f)
        except FileNotFoundError:
            self.q_table = {}

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.q_table, f)

    def get_state(self, metrics):
        return f"{metrics['calories']}_{metrics['form_score']}"

    def choose_action(self, state, epsilon=0.2):
        if random.random() < epsilon or state not in self.q_table:
            return random.choice(self.actions)
        return max(self.q_table[state], key=self.q_table[state].get)

    def update(self, state, action, reward, alpha=0.1, gamma=0.9):
        if state not in self.q_table:
            self.q_table[state] = {a: 0 for a in self.actions}
        old_value = self.q_table[state][action]
        new_value = old_value + alpha * (reward + gamma * max(self.q_table[state].values()) - old_value)
        self.q_table[state][action] = new_value
        self.save()