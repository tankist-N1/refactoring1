# Утилиты с дублирующим кодом
def print_header(text):
    print("=" * 50)
    print(text.center(50))
    print("=" * 50)

def validate_input(input_str):
    # Примитивная валидация
    if len(input_str) < 3:
        return False
    return True

# Избыточная функция, которая повторяет функционал TaskManager.show_all()
def display_tasks(tasks):
    for task in tasks:
        print(f"Задача: {task['name']}, Описание: {task['desc']}")