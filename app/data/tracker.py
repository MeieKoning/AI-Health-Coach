import json
from datetime import datetime

class Tracker:
    def __init__(self, filename="habit_log.json"):
        self.filename = filename
        try:
            with open(filename) as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}

    def log(self, key, value):
        timestamp = datetime.now().isoformat()
        self.data[timestamp] = {key: value}
        with open(self.filename, "w") as f:
            json.dump(self.data, f)

    def get_logs(self):
        return self.data