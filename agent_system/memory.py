import json
import os
MEMORY_FILE = "data/memory_store.json"

class Memory:
    def __init__(self):
        self.short_term = []
        self._ensure_file()


    def _ensure_file(self):
        if not os.path.exists(MEMORY_FILE):
            os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
            with open(MEMORY_FILE, 'w') as f:
                json.dump([], f)


    def add(self, user_input, plan, result):
        entry = {
            "input": user_input,
            "plan": plan, 
            "result": result
        }
        #short term memory
        self.short_term.append(entry)

        #long-term memory
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)

        data.append(entry)

        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=2)


    def get_recent(self, n=3):
        return self.short_term[-n:]
    
    def get_all(self):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
