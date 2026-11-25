import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "order.json")

class Database:
    def load_file(self):
        try:
            if not os.path.exists(FILENAME):
                return []
            else:
                with open(FILENAME, "r")as f:
                    data = json.load(f)
                return data

        except json.JSONDecodeError:
            return []

    def save_data(self, data):
        with open(FILENAME, "w")as f:
            json.dump(data, f, indent=4)
