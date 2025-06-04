from task_manager import TaskManager
from utils import print_header, validate_input, display_tasks
import sys

def run_app():
    tm = TaskManager()
    while True:
        # Слишком большая функция
        print_header("Менеджер задач")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Отметить выполненной")
        print("4. Показать все задачи")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Название: ")
            if not validate_input(name):
                print("Ошибка: название слишком короткое!")
                continue
            desc = input("Описание: ")
            tm.add(name, desc)
            print("Задача добавлена!")

        elif choice == "2":
            try:
                task_id = int(input("ID задачи для удаления: "))
                tm.delete(task_id)
            except ValueError:
                print("Ошибка: введите число!")
                
        elif choice == "3":
            try:
                task_id = int(input("ID задачи для отметки: "))
                tm.mark_done(task_id)
            except ValueError:
                print("Ошибка: введите число!")

        elif choice == "4":
            print_header("Список задач")
            tm.show_all()  # Использует метод класса
            print("\nДублирующий вывод через utils:")
            display_tasks(tm.tasks)  # Дублирование функционала

        elif choice == "5":
            sys.exit()

        else:
            print("Неверный ввод!")

if __name__ == "__main__":
    run_app()