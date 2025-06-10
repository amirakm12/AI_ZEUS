import json
import os

class ToDoSkill:
    def __init__(self, storage_path="todo_data.json"):
        self.storage_path = storage_path
        self.todos = self.load_todos()

    def load_todos(self):
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, "r") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def save_todos(self):
        with open(self.storage_path, "w") as f:
            json.dump(self.todos, f, indent=2)

    def add_todo(self, text):
        item = {"id": len(self.todos) + 1, "text": text, "done": False}
        self.todos.append(item)
        self.save_todos()
        return item

    def list_todos(self):
        return self.todos

    def mark_done(self, todo_id):
        for item in self.todos:
            if item["id"] == todo_id:
                item["done"] = True
        self.save_todos()

    def remove_todo(self, todo_id):
        self.todos = [item for item in self.todos if item["id"] != todo_id]
        self.save_todos()
