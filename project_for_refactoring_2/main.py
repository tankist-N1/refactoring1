from task_manager import TaskManager
from utils import print_tasks

def main():
    manager = TaskManager()
    while True:
        print("\nМеню:")
        print("1. Показать все задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Очистить список")
        print("5. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            print_tasks(manager.get_all())

        elif choice == "2":
            desc = input("Введите описание задачи: ").strip()
            if desc:
                manager.add(desc)
                print("Задача добавлена.")
            else:
                print("Описание не может быть пустым.")

        elif choice == "3":
            try:
                task_id = int(input("Введите ID задачи для удаления: "))
                if manager.delete(task_id):
                    print("Задача удалена.")
                else:
                    print("Задача с таким ID не найдена.")
            except ValueError:
                print("Ошибка: введите целое число.")

        elif choice == "4":
            confirm = input("Очистить все задачи? (y/n): ").strip().lower()
            if confirm == "y":
                manager.clear()
                print("Все задачи удалены.")

        elif choice == "5":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()