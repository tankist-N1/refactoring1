import json
import os


class TaskManager:
    def __init__(self, data_file: str = "tasks.json"):
        self.data_file = data_file
        self.tasks = []
        self._load()

    def _load(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as f:
                self.tasks = json.load(f)

    def _save(self):
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=4)

    def add(self, description: str):
        new_id = max((task["id"] for task in self.tasks), default=0) + 1
        self.tasks.append({"id": new_id, "description": description})
        self._save()

    def delete(self, task_id: int):
        original_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        if len(self.tasks) < original_len:
            self._save()
            return True
        return False

    def get_all(self):
        return self.tasks

    def clear(self):
        self.tasks = []
        self._save()
