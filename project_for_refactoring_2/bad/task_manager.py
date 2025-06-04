import json
from datetime import datetime

# Глобальная переменная (плохая практика)
DATA_FILE = "tasks.json"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load()  # Автозагрузка при инициализации

    def add(self, name, desc):
        # Добавляет задачу без валидации
        new_task = {
            "id": len(self.tasks) + 1,
            "name": name,
            "desc": desc,
            "done": False,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        self.tasks.append(new_task)
        self.save()

    def delete(self, task_id):
        # Удаляет задачу без проверки существования ID
        for t in self.tasks:
            if t["id"] == task_id:
                self.tasks.remove(t)
        self.save()

    def mark_done(self, task_id):
        # Отмечает задачу выполненной
        for t in self.tasks:
            if t["id"] == task_id:
                t["done"] = True
        self.save()

    def show_all(self):
        # Выводит задачи в консоль (нарушение SRP)
        for t in self.tasks:
            status = "✓" if t["done"] else "✗"
            print(f"{t['id']}. [{status}] {t['name']} - {t['desc']} ({t['date']})")

    def save(self):
        # Сохраняет в JSON
        with open(DATA_FILE, "w") as f:
            json.dump(self.tasks, f)

    def load(self):
        # Загружает из JSON
        try:
            with open(DATA_FILE, "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            print("Файл не найден. Создан новый список задач.")